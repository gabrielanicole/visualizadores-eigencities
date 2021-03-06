# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trayect', '0004_auto_20180111_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numa', models.CharField(max_length=50)),
                ('residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trayect.Antena')),
            ],
        ),
        migrations.RenameField(
            model_name='estadia',
            old_name='horaf',
            new_name='horaP',
        ),
        migrations.RemoveField(
            model_name='estadia',
            name='horai',
        ),
        migrations.AlterField(
            model_name='estadia',
            name='numa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trayect.Persona'),
        ),
    ]
