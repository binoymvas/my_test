# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170407_1032'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
        migrations.AlterModelTable(
            name='articleimage',
            table='article_images',
        ),
    ]
