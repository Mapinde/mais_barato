# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('barato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='data_criacao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
