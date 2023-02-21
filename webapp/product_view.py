from django.shortcuts import render
from webapp.models import Article
def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context=context)
