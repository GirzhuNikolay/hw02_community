from django.shortcuts import render, get_object_or_404
from .models import Post, Group


number_output_records = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:number_output_records]
    title = 'Главная страница Yatube'
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:number_output_records]
    template = 'posts/group_list.html'
    title = 'Информация групп Yatube'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, template, context)
