# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0004_auto_20180412_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='users',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to='belt.User'),
            preserve_default=False,
        ),
    ]
