# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-17 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna_esc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=4, max_digits=9)),
                ('zoom', models.IntegerField(default=10)),
                ('pob_Comun_2002', models.IntegerField(default=10)),
                ('vehicle', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('motor', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Non_motorized', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('private_transport', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('public_transport', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('CO2_transport', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Green', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Iliteracy', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Municipal_spending', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Unemployment', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Crime', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Arrested', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Companies', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Sales', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('workers', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Income', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('technicians', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('University', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Professionals', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Solid_waste', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Municipal_Power', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Municipal_Water', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Municipal_cleaning', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Deaths', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Birthrate', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Year_scholarship', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Offence_Property', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Offence_Person', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Burglary', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Robbery', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Injuries', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Indigenous', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Emergency', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Respiratory', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Cardiovascular', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Hospitalizations', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('Street', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conurbacion_esc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=4, max_digits=9)),
                ('zoom', models.IntegerField(default=10)),
                ('pob_Conurb_2002', models.IntegerField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='comuna_esc',
            name='conurbacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='escalamiento.Conurbacion_esc'),
        ),
    ]
