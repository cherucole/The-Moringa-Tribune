# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='', upload_to='articles/'),
        ),
    ]
