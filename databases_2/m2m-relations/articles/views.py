from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    all_articles = Article.objects.all()

    context = {
        'object_list': all_articles,

    }


    return render(request, template, context)
