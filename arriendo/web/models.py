from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Usuario(models.Model):
    usu_rut = models.CharField(primary_key=True, max_length=12)
    usu_nombres = models.CharField(max_length=50, blank=True, null=True)
    usu_apepat = models.CharField(max_length=30, blank=True, null=True)
    usu_apemat = models.CharField(max_length=30, blank=True, null=True)
    usu_direccion = models.CharField(max_length=100, blank=True, null=True)
    usu_telefono = models.CharField(max_length=20, blank=True, null=True)
    usu_mail = models.CharField(max_length=30, blank=True, null=True)
    tu = models.ForeignKey('TipoUsuario', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class TipoUsuario(models.Model):
    tu_id = models.AutoField(primary_key=True)
    tu_nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Inmueble(models.Model):
    inm_id = models.AutoField(primary_key=True)
    inm_nombre = models.CharField(max_length=30, blank=True, null=True)
    inm_descripcion = models.CharField(max_length=100, blank=True, null=True)
    inm_m2_construidos = models.FloatField(blank=True, null=True)
    inm_m2_total = models.FloatField(blank=True, null=True)
    inm_cant_estacionamientos = models.IntegerField(blank=True, null=True)
    inm_cant_habitaciones = models.IntegerField(blank=True, null=True)
    inm_cant_banos = models.IntegerField(blank=True, null=True)
    inm_direccion = models.CharField(max_length=100, blank=True, null=True)
    ti_codigo = models.ForeignKey('TipoInmueble', models.DO_NOTHING, db_column='ti_codigo', blank=True, null=True)
    inm_precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmueble'


class Region(models.Model):
    reg_codigo = models.CharField(primary_key=True, max_length=5)
    reg_nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class Comuna(models.Model):
    comuna_codigo = models.CharField(primary_key=True, max_length=10)
    comuna_nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class TipoInmueble(models.Model):
    ti_codigo = models.AutoField(primary_key=True)
    ti_nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_inmueble'
