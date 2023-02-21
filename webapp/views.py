from django.shortcuts import render
from webapp.models import Article
from webapp.models import Category
def index_view(request):
    articles = Article.objects.all()
    categories= Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'index.html', context)