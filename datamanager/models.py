# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Geo(models.Model):
    geoid = models.BigIntegerField(db_column='GEOID', blank=False, null=False, primary_key=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo'


class Tidychampaign(models.Model):
    geoid = models.BigIntegerField(db_column='GEOID', blank=False, null=False, primary_key=True)  # Field name made lowercase.
    block = models.TextField(db_column='Block', blank=True, null=True)  # Field name made lowercase.
    geography = models.TextField(db_column='Geography', blank=True, null=True)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    white = models.IntegerField(db_column='White', blank=True, null=True)  # Field name made lowercase.
    black = models.IntegerField(db_column='Black', blank=True, null=True)  # Field name made lowercase.
    asian = models.IntegerField(db_column='Asian', blank=True, null=True)  # Field name made lowercase.
    otherrace = models.IntegerField(db_column='OtherRace', blank=True, null=True)  # Field name made lowercase.
    male = models.IntegerField(db_column='Male', blank=True, null=True)  # Field name made lowercase.
    female = models.IntegerField(db_column='Female', blank=True, null=True)  # Field name made lowercase.
    young = models.IntegerField(db_column='Young', blank=True, null=True)  # Field name made lowercase.
    middle = models.IntegerField(db_column='Middle', blank=True, null=True)  # Field name made lowercase.
    old = models.IntegerField(db_column='Old', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tidychampaign'

class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    race = models.CharField(max_length=20)
    geoid = models.BigIntegerField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'UserInfo'