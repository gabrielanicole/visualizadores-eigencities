# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-11 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trayect', '0003_auto_20180105_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='antena',
            name='habitantesTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='antena',
            name='residentesTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
