from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200,null=False,blank=False, verbose_name='titile')
    text = models.TextField(max_length=3000, null=False,blank=False,verbose_name='text')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='category')
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    cost = models.DecimalField(verbose_name='cost', max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', verbose_name='image')

    def __str__(self):
        return f'{self.title} -{self.text} -{self.cost}'

class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=200,null=False,blank=False )
    text = models.CharField(verbose_name='text', max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.title} -{self.text}'