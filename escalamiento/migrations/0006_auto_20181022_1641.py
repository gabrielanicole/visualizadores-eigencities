# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-22 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalamiento', '0005_auto_20181022_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna_esc',
            name='pob_Comun_2602',
        ),
        migrations.AddField(
            model_name='comuna_esc',
            name='pob_Comun_2002',
            field=models.IntegerField(default=10),
        ),
    ]
