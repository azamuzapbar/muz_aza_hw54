# Generated by Django 4.1.7 on 2023-02-21 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('text', models.CharField(blank=True, max_length=200, null=True, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titile')),
                ('text', models.TextField(max_length=3000, verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cost')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.category', verbose_name='category')),
            ],
        ),
    ]
