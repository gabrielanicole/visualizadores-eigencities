# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='discapac_0',
            field=models.IntegerField(blank=True, db_column='DISCAPAC_0', null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='discapac_1',
            field=models.IntegerField(blank=True, db_column='DISCAPAC_1', null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='discapac_t',
            field=models.IntegerField(blank=True, db_column='DISCAPAC_T', null=True),
        ),
    ]