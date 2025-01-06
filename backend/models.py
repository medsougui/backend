from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now


class Products(models.Model):
    idp = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    nbstock = models.IntegerField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Producttype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producttype'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)
    photo = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'auth_user'