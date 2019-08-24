from django.urls import path
from chat import consumers, views

websocket_urlpatterns = [
    path('chat/', consumers.ChatConsumer)
]

urlpatterns = [
    path('chat/ui/', views.chat_interface, name='chat-interface')
]
