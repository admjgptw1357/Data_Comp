# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'competition name')),
                ('description', models.TextField(blank=True, verbose_name=b'description')),
                ('contest_type', models.CharField(choices=[('Regression', b'regression'), ('Classification', b'classification'), ('Clustering', b'clustering')], default=b'regression', max_length=20, verbose_name=b'contest type')),
                ('scoring', models.CharField(choices=[('MSE', 'MSE'), ('RMSE', 'RMSE'), ('Correlation', 'CORRELATION'), ('Accuracy', 'ACCURACY'), ('F1', 'F1'), ('Adjusted Rand Score', 'ADJUSTED RAND SCORE')], default=b'RMSE', max_length=20, verbose_name=b'scoring method')),
                ('data_number', models.IntegerField(verbose_name=b'answer data size')),
                ('answer', models.TextField(verbose_name=b'answer')),
                ('mid_test_s', models.IntegerField(default=0, verbose_name=b'start index of mid test')),
                ('mid_test_e', models.IntegerField(default=0, verbose_name=b'end index of mid test')),
                ('f_test_s', models.IntegerField(default=0, verbose_name=b'start index of final test')),
                ('f_test_e', models.IntegerField(default=0, verbose_name=b'end index of final test')),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name=b'User ID')),
                ('mid_result', models.DecimalField(decimal_places=6, max_digits=12, verbose_name=b'mid result')),
                ('f_result', models.DecimalField(decimal_places=6, max_digits=12, verbose_name=b'final result')),
                ('submission_date', models.DateTimeField()),
                ('short_comment', models.CharField(blank=True, max_length=255, verbose_name=b'Short Comment')),
                ('competition_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to='app.Competition', verbose_name=b'Competition name')),
            ],
        ),
    ]
