from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'title': 'The river between',
        'author': 'Ngugi wa thiongo',
        'content': 'First book i ever wrote',
        'date_posted': 'July 2, 2021'
    },
    {
        'title': 'Once upon time in hollywood',
        'author': 'Leonardo decaprio & Brad pitt',
        'content': 'First book i ever wrote',
        'date_posted': 'July 2, 2021'
    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})