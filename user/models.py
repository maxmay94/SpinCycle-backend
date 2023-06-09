from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from enum import Enum


class StateChoices(Enum):
    MA = 'Massachusetts'
    NH = 'New Hampshire'
    ME = 'Maine'
    VT = 'Vermont'
    RI = 'Rhode Island'
    CT = 'Connecticut'
    NY = 'New York'
    NJ = 'New Jersey'
    PA = 'Pennsylvania'
    DE = 'Delaware'
    MD = 'Maryland'
    VA = 'Virginia'
    WV = 'West Virginia'
    NC = 'North Carolina'
    SC = 'South Carolina'
    GA = 'Georgia'
    FL = 'Florida'
    AL = 'Alabama'
    MS = 'Mississippi'
    TN = 'Tennessee'
    KY = 'Kentucky'
    OH = 'Ohio'
    MI = 'Michigan'
    IN = 'Indiana'
    IL = 'Illinois'
    WI = 'Wisconsin'
    MN = 'Minnesota'
    IA = 'Iowa'
    MO = 'Missouri'
    AR = 'Arkansas'
    LA = 'Louisiana'
    ND = 'North Dakota'
    SD = 'South Dakota'
    NE = 'Nebraska'
    KS = 'Kansas'
    OK = 'Oklahoma'
    TX = 'Texas'
    MT = 'Montana'
    WY = 'Wyoming'
    CO = 'Colorado'
    NM = 'New Mexico'
    ID = 'Idaho'
    UT = 'Utah'
    AZ = 'Arizona'
    NV = 'Nevada'
    WA = 'Washington'
    OR = 'Oregon'
    CA = 'California'
    AK = 'Alaska'
    HI = 'Hawaii'


# Create your models here.

# User Class
class User(models.Model):
    USER_CUSTOMER = 'customer'
    USER_SERVICE_PROVIDER = 'service_provider'
    USER_DRIVER = 'driver'
    USER_TYPE_CHOICES = [
        (USER_CUSTOMER, 'Customer'),
        (USER_SERVICE_PROVIDER, 'Service Provider'),
        (USER_DRIVER, 'Driver'),
    ]
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=21, choices=USER_TYPE_CHOICES, default=USER_CUSTOMER)

# Address Class
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    street_address_line_1 = models.CharField(max_length=100)
    street_address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    # Maybe? vvv
    state = models.CharField(max_length=2, choices=[(state.name, state.value) for state in StateChoices])
    zip_code = models.CharField(max_length=20)
    country = CountryField() 
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

# Driver Class
class Driver(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    vehicle_type = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    driver_picture = models.ImageField(upload_to='driver_pictures/', default='driver_pictures/default.jpg')

# Customer Class
class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    laundry_preferences = models.JSONField()
    # order_history = order/model
    