from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
def home(request):
    # posts = [
    #     {'author': 'Rania Fahmy', 'title': 'Blog Post 1', 'content': 'First post content', 'date_posted': 'August 27, 2019'},
    #     {'author': 'Mazey Star', 'title': 'Fade into You', 'content': 'I wanna bla bla bla', 'date_posted': 'October 22, 2020'}
    # ]
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

