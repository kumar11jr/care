# Generated by Django 4.2.2 on 2023-08-22 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "facility",
            "0379_rename_prescribed_medication_patientconsultation_treatment_plan",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="patientnotes",
            name="user_type",
            field=models.CharField(default="", max_length=25),
        ),
    ]