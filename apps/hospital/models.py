from django.db import models
from django.utils import timezone


class PatientModel(models.Model):
    name = models.CharField(verbose_name="Patient Name", max_length=150)
    age = models.SmallIntegerField(verbose_name="Patient Age")
    address = models.CharField(verbose_name="Patient Address", max_length=255)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return f"{self.name}"


class ExamModel(models.Model):
    professionals_name = models.CharField(
        verbose_name="Professional's Name", max_length=150
    )
    registration_date = models.DateTimeField(
        default=timezone.now, verbose_name="Registration Date"
    )
    weight = models.FloatField(verbose_name="Patient Weight")
    height = models.FloatField(verbose_name="Patient Height")
    patient = models.ForeignKey(
        PatientModel,
        verbose_name="Patient",
        related_name="patient",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"

    def __str__(self):
        return f"Exam for {self.patient.name}"
