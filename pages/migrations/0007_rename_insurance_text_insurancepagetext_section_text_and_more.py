# Generated by Django 5.1.3 on 2025-01-17 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_insurancepagetext"),
    ]

    operations = [
        migrations.RenameField(
            model_name="insurancepagetext",
            old_name="insurance_text",
            new_name="section_text",
        ),
        migrations.AddField(
            model_name="insurancepagetext",
            name="name_of_section",
            field=models.CharField(default="To change", max_length=255),
            preserve_default=False,
        ),
    ]
