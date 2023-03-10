from django.shortcuts import render, get_object_or_404
from .models import Post, Group


number_output_records = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:number_output_records]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug=None):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:number_output_records]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
