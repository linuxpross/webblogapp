from django.shortcuts import render, get_object_or_404, redirect  # Добавлен импорт redirect
from .models import Post, Message  # Импорт Message добавлен здесь
from django.utils import timezone
from .forms import MessageForm  # Импортируем MessageForm из вашего файла форм

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/blogg.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def chat_room(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_room')
    else:
        form = MessageForm()

    messages = Message.objects.all()
    return render(request, 'chat/chat_room.html', {'messages': messages, 'form': form})