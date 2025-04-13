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
    accepting_clients = models.CharField(max_length=50)
    certifications = models.ManyToManyField(Certification)
    insurances = models.ManyToManyField(Insurance)
    populations = models.ManyToManyField(Population)
    bio = models.TextField()
    picture_filename = models.CharField(max_length=50, default="ofarrell_ryan.jpg")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.license_type}"

    def to_insurances_string(self):
        return ", ".join(self.insurances.all().values_list("name", flat=True))

    def to_populations_string(self):
        return ", ".join(self.populations.all().values_list("group", flat=True))

    def to_certifications_string(self):
        return ", ".join(self.insurances.all().values_list("name", flat=True))


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question


class InsurancePageText(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self) -> str:
        return self.name


class AboutUs(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return "About us"

    class Meta:
        verbose_name_plural = "About us"
