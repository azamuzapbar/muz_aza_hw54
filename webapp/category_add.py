from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.models import Category

def add_category(request):
    if request.method == 'GET':
        return render(request, 'add_category.html')
    elif request.method == 'POST':
        category_data = {
            'title': request.POST.get('title'),
            'text': request.POST.get('text'),
        }
    category = Category.objects.create(**category_data)
    return redirect(reverse('index'))