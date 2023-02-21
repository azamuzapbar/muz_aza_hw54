from webapp.views import index_view
from webapp.product_view import article_view
from webapp.product_add import add_view
from webapp.category_add import add_category
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', index_view, name='index'),
    path('products/', index_view,name='products'),
    path('article/<int:pk>', article_view, name='detailed_view'),
    path('article/add/', add_view, name='article_add'),
    path('category/add/', add_category, name='add_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)