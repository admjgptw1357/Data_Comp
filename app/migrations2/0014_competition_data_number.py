# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160618_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='data_number',
            field=models.IntegerField(default=596, verbose_name=b'answer data size'),
            preserve_default=False,
        ),
    ]