from django.db import models
from django.urls import reverse
from bloodbanks.choices import *
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

User = get_user_model()


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined = models.DateTimeField(auto_now_add=True)
    blood_group = models.CharField(max_length=50, choices=BlOOD_GROUP_CHOICE)
    genotype = models.CharField(max_length=50, choices=GENOTYPE_CHOICE)
    sex = models.CharField(max_length=50, choices=SEX_CHOICE)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=700)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    country = CountryField(blank_label='(select country)')
    zipcode = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False)
    will_donate = models.CharField(max_length=50, choices=WILL_DONATE)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return self.user.first_name + "Donor Details"

