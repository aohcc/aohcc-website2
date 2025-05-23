# Generated by Django 5.1.3 on 2025-01-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_therapist_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Population",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="therapist",
            name="populations",
            field=models.ManyToManyField(to="pages.population"),
        ),
    ]
