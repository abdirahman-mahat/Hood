# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-26 08:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_category_comment_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
