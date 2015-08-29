# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('nombre', models.CharField(max_length=50, null=True, db_column='NOMBRE', blank=True)),
                ('ddcia', models.CharField(max_length=50, null=True, db_column='DDCIA', blank=True)),
                ('rbd', models.IntegerField(serialize=False, primary_key=True, db_column='RBD', blank=True)),
            ],
            options={
                'db_table': 'Establecimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('localidad_Establecimiento', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='appsim.Establecimiento', blank=True)),
                ('region', models.CharField(max_length=50, null=True, db_column='REGION', blank=True)),
                ('prov', models.CharField(max_length=50, null=True, db_column='PROV', blank=True)),
                ('comuna', models.CharField(max_length=50, null=True, db_column='COMUNA', blank=True)),
            ],
            options={
                'db_table': 'Localidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PruebaCienciasNaturales',
            fields=[
                ('Ciencias_Establecimiento', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='appsim.Establecimiento', blank=True)),
                ('alum_nat', models.IntegerField(null=True, db_column='ALUM_NAT', blank=True)),
                ('prom_nat', models.FloatField(null=True, db_column='PROM_NAT', blank=True)),
            ],
            options={
                'db_table': 'Prueba_Ciencias_Naturales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PruebaLectura',
            fields=[
                ('Lectura_Establecimiento', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='appsim.Establecimiento', blank=True)),
                ('alum_lect', models.IntegerField(null=True, db_column='ALUM_LECT', blank=True)),
                ('prom_lect', models.FloatField(null=True, db_column='PROM_LECT', blank=True)),
            ],
            options={
                'db_table': 'Prueba_Lectura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PruebaMatematicas',
            fields=[
                ('matematicas_Establecimiento', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='appsim.Establecimiento', blank=True)),
                ('alum_mat', models.IntegerField(null=True, db_column='ALUM_MAT', blank=True)),
                ('prom_mat', models.FloatField(null=True, db_column='PROM_MAT', blank=True)),
            ],
            options={
                'db_table': 'Prueba_Matematicas',
                'managed': False,
            },
        ),
    ]
