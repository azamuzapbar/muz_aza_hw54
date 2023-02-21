from django.shortcuts import render, redirect
from django.urls import reverse
from webapp.models import Article
from webapp.models import Category
def add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'article_add.html', context)
    elif request.method == "POST":
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        article_data = {
            'title': request.POST.get('title'),
            'cost': request.POST.get('cost'),
            'image': request.POST.get('image'),
            'category': category,
            'text': request.POST.get('text')
        }
        article = Article.objects.create(**article_data)
        return redirect(reverse('detailed_view', kwargs={'pk': article.pk}))