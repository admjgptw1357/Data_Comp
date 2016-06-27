# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-19 03:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20160619_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user_id',
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]