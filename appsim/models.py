# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Establecimiento(models.Model):
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddcia = models.CharField(db_column='DDCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rbd = models.IntegerField(db_column='RBD', primary_key=True, blank=True, null=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Establecimiento'


class Localidad(models.Model):
    localidad_Establecimiento = models.OneToOneField(Establecimiento, db_column='id',primary_key=True, blank=True, null=False)
    region = models.CharField(db_column='REGION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prov = models.CharField(db_column='PROV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comuna = models.CharField(db_column='COMUNA', max_length=50, blank=True, null=True)  # Field name made lowercase.
  

    class Meta:
        managed = False
        db_table = 'Localidad'


class PruebaCienciasNaturales(models.Model):
    Ciencias_Establecimiento = models.OneToOneField(Establecimiento, db_column='id',primary_key=True, blank=True, null=False)
    alum_nat = models.IntegerField(db_column='ALUM_NAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prom_nat = models.FloatField(db_column='PROM_NAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    
    class Meta:
        managed = False
        db_table = 'Prueba_Ciencias_Naturales'

class PruebaLectura(models.Model):
    Lectura_Establecimiento = models.OneToOneField(Establecimiento, db_column='id',primary_key=True, blank=True, null=False)
    alum_lect = models.IntegerField(db_column='ALUM_LECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prom_lect = models.FloatField(db_column='PROM_LECT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.


    class Meta:
        managed = False
        db_table = 'Prueba_Lectura'


class PruebaMatematicas(models.Model):
    matematicas_Establecimiento = models.OneToOneField(Establecimiento, db_column='id',primary_key=True, blank=True, null=False)
    alum_mat = models.IntegerField(db_column='ALUM_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prom_mat = models.FloatField(db_column='PROM_MAT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Prueba_Matematicas'
