# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-27 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalamiento', '0009_variable_fuente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='descripcion',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
