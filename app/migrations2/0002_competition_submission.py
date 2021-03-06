# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name=b'competition name')),
                ('description', models.TextField(blank=True, verbose_name=b'description')),
                ('scoring', models.CharField(choices=[('MSE', 'MSE'), ('RMSE', 'RMSE'), ('COR', 'CORRELATION'), ('ACC', 'ACCURACY'), ('F1', 'F1'), ('CLS', 'ADJUSTED RAND SCORE')], default=b'RMSE', max_length=5, verbose_name=b'scoring method')),
                ('answer', models.TextField(verbose_name=b'answer')),
                ('mid_test_s', models.IntegerField(default=0, verbose_name=b'start index of mid test')),
                ('mid_test_e', models.IntegerField(default=0, verbose_name=b'end index of mid test')),
                ('f_test_s', models.IntegerField(default=0, verbose_name=b'start index of final test')),
                ('f_test_e', models.IntegerField(default=0, verbose_name=b'end index of final test')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name=b'User ID')),
                ('mid_result', models.DecimalField(decimal_places=6, max_digits=8)),
                ('f_result', models.DecimalField(decimal_places=6, max_digits=8)),
                ('submission_date', models.DateField()),
                ('competition_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Submission', to='app.Competition', verbose_name=b'Competition name')),
            ],
        ),
    ]
