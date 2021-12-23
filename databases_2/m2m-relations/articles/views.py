from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    all_articles = Article.objects.all().prefetch_related('theme').order_by('-published_at')

    context = {
        'object_list': all_articles,

    }


    return render(request, template, context)
