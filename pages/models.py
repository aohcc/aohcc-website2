from django.db import models


class Certification(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.name


class Insurance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Population(models.Model):
    group = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.group


class Therapist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_type = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    certifications = models.ManyToManyField(Certification)
    insurances = models.ManyToManyField(Insurance)
    populations = models.ManyToManyField(Population)
    bio = models.TextField()
    picture = models.ImageField(upload_to="static/bio_pics", default=None)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.license_type}"
