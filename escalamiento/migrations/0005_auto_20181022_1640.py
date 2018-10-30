# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-22 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escalamiento', '0004_auto_20181022_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comuna_esc',
            name='pob_Comun_2002',
        ),
        migrations.AddField(
            model_name='comuna_esc',
            name='pob_Comun_2602',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Arrested',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Birthrate',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Burglary',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='CO2_transport',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Cardiovascular',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Companies',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Crime',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Deaths',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Emergency',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Green',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Hospitalizations',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Iliteracy',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Income',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Indigenous',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Injuries',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Municipal_Power',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Municipal_Water',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Municipal_cleaning',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Municipal_spending',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Non_motorized',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Offence_Person',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Offence_Property',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Professionals',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Respiratory',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Robbery',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Sales',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Solid_waste',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Street',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Unemployment',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='University',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='Year_scholarship',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='motor',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='private_transport',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='public_transport',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='technicians',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='vehicle',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='comuna_esc',
            name='workers',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='conurbacion_esc',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
        migrations.AlterField(
            model_name='conurbacion_esc',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=26, null=True),
        ),
    ]