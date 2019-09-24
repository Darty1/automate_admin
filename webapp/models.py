from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    date_of_birth = models.DateField(auto_now=False, null=True)
    address = models.TextField(max_length=200, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+375336251926'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, null=True)
    email = models.EmailField(max_length=100, null=True)


class Admin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=100)


class Car(models.Model):

    year = models.IntegerField(null=True)
    vin_regex = RegexValidator(regex=r'^\d{1}[A-Z]{4}\d{2}[A-Z]{4}\d{6}$',
                                 message="VIN must be entered in the format: '1HGBH41JXMN109186'. Up to 15 digits allowed.")
    vin = models.CharField(validators=[vin_regex], max_length=17, null=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=32, null=True)
    model = models.CharField(max_length=32, null=True)


class Order(models.Model):
    date = models.DateField(auto_now=False)
    amount = models.DecimalField(max_digits=5, decimal_places=1)
    status = models.CharField(max_length=1, choices=(('1', 'Completed'), ('2', 'In Progress'),
                                                     ('3', 'Cancelled')), null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)








