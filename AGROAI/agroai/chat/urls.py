from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_interface, name='chat_interface'),
    path('conversation/<int:conversation_id>/', views.chat_interface, name='chat_conversation'),
    path('api/conversations/', views.get_conversations, name='get_conversations'),
    path('api/process-message/', views.process_message, name='process_message'),
]