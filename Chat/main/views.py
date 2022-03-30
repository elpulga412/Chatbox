from django.shortcuts import render
from .models import Chat
# Create your views here.

def index(request):
    chats= Chat.objects.all()
    context = {'chats': chats}
    return render(request, 'chat/chat_room.html', context)