# Generated by Django 4.2.6 on 2023-11-14 16:49

from django.db import migrations


def free_discharged_beds(apps, schema_editor):
    PatientConsultation = apps.get_model("facility", "PatientConsultation")
    ConsultationBed = apps.get_model("facility", "ConsultationBed")

    for consultation in PatientConsultation.objects.filter(
        discharge_date__isnull=False
    ):
        ConsultationBed.objects.filter(
            consultation=consultation, end_date__isnull=True
        ).update(end_date=consultation.discharge_date)


class Migration(migrations.Migration):
    dependencies = [
        (
            "facility",
            "0393_rename_diagnosis_patientconsultation_deprecated_diagnosis_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(free_discharged_beds, migrations.RunPython.noop),
    ]