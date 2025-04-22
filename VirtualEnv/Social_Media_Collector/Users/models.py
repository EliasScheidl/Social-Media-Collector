# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classes(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    department = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classes'
        unique_together = (('name', 'department'),)


class Departments(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'

class Profiles(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.TextField(unique=True)
    role = models.TextField()
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_field = models.ForeignKey(Classes, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'profiles'

class SupabaseUser(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.EmailField()
    encrypted_password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    last_sign_in_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = '"auth"."users"'