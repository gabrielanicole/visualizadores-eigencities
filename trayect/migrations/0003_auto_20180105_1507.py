# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-05 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trayect', '0002_remove_antindic_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antindic',
            name='cantidad',
            field=models.DecimalField(decimal_places=4, max_digits=9),
        ),
    ]
