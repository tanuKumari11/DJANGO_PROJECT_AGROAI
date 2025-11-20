from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from .models import Conversation, Message
from .ai_processor import AgroAIProcessor

def home(request):
    return render(request, 'chat/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/chat/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'chat/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif len(password1) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
        else:
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                return redirect('chat_interface')
    
    return render(request, 'chat/register.html')

@login_required
def chat_interface(request, conversation_id=None):
    if conversation_id:
        conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
    else:
        # Get or create a default conversation
        conversation, created = Conversation.objects.get_or_create(
            user=request.user,
            title="New Conversation",
            defaults={'title': 'New Conversation'}
        )
        conversation_id = conversation.id
    
    return render(request, 'chat/chat_interface.html', {
        'conversation': conversation,
        'conversation_id': conversation_id
    })

@login_required
def get_conversations(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-updated_at')
    data = [{
        'id': conv.id,
        'title': conv.title,
        'updated_at': conv.updated_at.strftime('%Y-%m-%d %H:%M')
    } for conv in conversations]
    return JsonResponse(data, safe=False)

@login_required
@csrf_exempt
def process_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            conversation_id = data.get('conversation_id')
            message = data.get('message')
            
            if not conversation_id or not message:
                return JsonResponse({'success': False, 'error': 'Missing conversation_id or message'})
            
            conversation = get_object_or_404(Conversation, id=conversation_id, user=request.user)
            
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
            
            # Update conversation title if it's the first message
            if conversation.messages.count() == 2:  # User message + AI response
                conversation.title = message[:50] + "..." if len(message) > 50 else message
                conversation.save()
            
            return JsonResponse({
                'success': True,
                'response': response,
                'message_id': ai_message.id
            })
        
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})