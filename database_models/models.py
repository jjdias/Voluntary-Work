from django.db import models

# Phone validator. Link at the end.
from django.core.validators import RegexValidator


# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length=140)
    date_birth = models.DateField()
    email = models.EmailField()

    # For verifying the phone.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list

    def __str__(self):
        return self.name


# Phone verification: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models