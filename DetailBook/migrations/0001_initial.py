# Generated by Django 4.2.6 on 2023-10-27 12:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Homepage', '0007_rename_last_edit_time_book_user_last_edit_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImageUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Homepage.book')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('language', models.CharField(max_length=10)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('currencyCode', models.CharField(blank=True, max_length=10, null=True)),
                ('is_ebook', models.BooleanField()),
                ('pdf_available', models.BooleanField()),
                ('pdf_link', models.URLField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('saleability', models.BooleanField(default=False)),
                ('buy_link', models.URLField(blank=True, null=True)),
                ('epub_available', models.BooleanField(default=False)),
                ('epub_link', models.URLField(blank=True, null=True)),
                ('maturity_rating', models.CharField(max_length=25)),
                ('page_count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('user_publish_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user_last_edit_time', models.DateTimeField(blank=True, null=True)),
                ('authors', models.ManyToManyField(related_name='authors_book', to='DetailBook.author')),
                ('categories', models.ManyToManyField(related_name='book_categories', to='DetailBook.category')),
                ('images', models.ManyToManyField(to='DetailBook.imageurl')),
            ],
        ),
    ]