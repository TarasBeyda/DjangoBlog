from django.shortcuts import render
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
