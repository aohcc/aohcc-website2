from django.db import models


class Credential(models.Model):
    name = models.CharField(max_length=75)


class Insurance(models.Model):
    name = models.CharField(max_length=50)


class Therapist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    credentials = models.ManyToManyField(Credential)
    insurances = models.ManyToManyField(Insurance)
