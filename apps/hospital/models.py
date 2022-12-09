from django.db import models
from django.utils import timezone


class PatientModel(models.Model):
    name = models.CharField(verbose_name="Patient Name", max_length=150)
    age = models.SmallIntegerField()


class PatientAddressModel(models.Model):
    country = models.CharField(verbose_name="Country Name", max_length=150)
    state = models.CharField(verbose_name="State Name", max_length=150)
    district = models.CharField(verbose_name="District Name", max_length=150)
    street = models.CharField(verbose_name="Street Name/Number", max_length=150)
    place_number = models.SmallIntegerField(verbose_name="Place Number")
    patient = models.ForeignKey(
        PatientModel,
        verbose_name="Patient",
        related_name="patient_address",
        on_delete=models.CASCADE,
        unique=True
    )


class ExamModel(models.Model):
    professionals_name = models.CharField(
        verbose_name="Professional's Name", max_length=150
    )
    registration_date = models.DateField(
        default=timezone.now, verbose_name="Registration Date"
    )
    weight = models.FloatField(verbose_name="Patient Weight")
    height = models.FloatField(verbose_name="Patient Height")
    patient = models.ForeignKey(
        PatientModel,
        verbose_name="Patient",
        related_name="patient",
        on_delete=models.PROTECT
    )
