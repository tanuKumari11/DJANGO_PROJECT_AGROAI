import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Conversation, Message
from .ai_processor import AgroAIProcessor

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f'chat_{self.conversation_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        conversation_id = text_data_json['conversation_id']

        # Process message with AgroAI
        response = await self.process_ai_message(message, conversation_id)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': response
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def process_ai_message(self, message, conversation_id):
        conversation = Conversation.objects.get(id=conversation_id)
        
        # Save user message
        user_message = Message.objects.create(
            conversation=conversation,
            content=message,
            is_user=True
        )
        
        # Process with AgroAI
        ai_processor = AgroAIProcessor()
        response = ai_processor.process_message(message, conversation)
        
        # Save AI response
        ai_message = Message.objects.create(
            conversation=conversation,
            content=response['content'],
            is_user=False,
            message_type=response.get('type', 'text')
        )
        
        return response