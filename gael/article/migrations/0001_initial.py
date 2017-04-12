# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Published On')),
                ('category', models.IntegerField(default=0)),
                ('hero_image', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=200)),
                ('article_image', models.ImageField(default='None', upload_to='article_images')),
                ('optional_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Article Images',
            },
        ),
    ]
