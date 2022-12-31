from django.shortcuts import render
from .models import blog

def index(request):
    context = {
        'content': 'selamat datang',
    }
    return render(request, 'index.html', context)


def blogs(request):
    blogs = blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)
