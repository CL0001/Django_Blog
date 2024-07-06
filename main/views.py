from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True)
    posts = Blog.objects.filter(is_featured=False)
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts
    }
    return render(request, 'home.html', context)