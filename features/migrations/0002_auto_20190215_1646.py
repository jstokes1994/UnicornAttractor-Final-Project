# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='feature',
            name='money_donated',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='status',
            field=models.CharField(choices=[('N', 'Not Started'), ('I', 'In Development'), ('D', 'Done')], default='N', max_length=1),
        ),
    ]
