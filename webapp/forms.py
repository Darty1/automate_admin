import datetime

from django.contrib.admin.widgets import AdminDateWidget

from django.forms import *
from .models import *


class AdminForm(Form):
    username = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    password = CharField(min_length=3, max_length=32, widget=PasswordInput({'class': 'form-control'}))


class UserForm(Form):
    first_name = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    last_name = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    date_of_birth = DateField(initial=datetime.date.today, widget=DateInput({'class': 'datepicker'}),
                              input_formats=('%m/%d/%Y',))
    address = CharField(widget=TextInput({'class': 'form-control'}))
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = CharField(validators=[phone_regex], max_length=17, widget=TextInput({'class': 'form-control'}))
    email = EmailField(min_length=5, max_length=40, widget=EmailInput({'class': 'form-control'}))


class CarForm(Form):
    make = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    model = CharField(min_length=3, max_length=32, widget=TextInput({'class': 'form-control'}))
    year = IntegerField(widget=NumberInput({'class': 'form-control'}))
    vin_regex = RegexValidator(regex=r'^\d{1}[A-Z]{4}\d{2}[A-Z]{4}\d{6}$',
                               message="VIN must be entered in the format: '1HGBH41JXMN109186'. Up to 15 digits allowed.")
    vin = CharField(validators=[vin_regex], max_length=17, widget=TextInput({'class': 'form-control'}))


class OrderForm(Form):
    from .models import Car
    date = DateField(widget=DateInput({'class': 'form-control'}))
    amount = DecimalField(widget=TextInput({'class': 'form-control'}))
    status = MultipleChoiceField(required=False, choices=(('1', 'Completed'), ('2', 'In Progress'),
                                                          ('3', 'Cancelled')),
                                 widget=CheckboxInput({'class': 'form-control'}))
