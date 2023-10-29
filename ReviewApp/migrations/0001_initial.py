# Generated by Django 4.2.5 on 2023-10-24 14:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('language', models.CharField(max_length=10)),
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
                ('authors', models.ManyToManyField(related_name='authors_book', to='ReviewApp.author')),
                ('categories', models.ManyToManyField(related_name='book_categories', to='ReviewApp.category')),
                ('images', models.ManyToManyField(to='ReviewApp.imageurl')),
            ],
        ),
    ]