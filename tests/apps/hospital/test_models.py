from django.db import models
from django.utils import timezone

from apps.hospital.models import PatientModel, ExamModel


class TestPatientModel:
    @classmethod
    def setup_class(cls):
        cls.model = PatientModel

    def test_str(self):
        patient = PatientModel(name="foo")

        assert str(patient) == "foo"

    def test_parent_class(self):
        assert issubclass(PatientModel, models.Model)

    def test_meta_verbose_name(self):
        assert self.model._meta.verbose_name == "Patient"

    def test_meta_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Patients"

    def test_name_field(self):
        field = self.model._meta.get_field("name")

        assert type(field) == models.CharField
        assert field.verbose_name == "Patient Name"
        assert field.max_length == 150

    def test_age_field(self):
        field = self.model._meta.get_field("age")

        assert type(field) == models.SmallIntegerField
        assert field.verbose_name == "Patient Age"

    def test_address_field(self):
        field = self.model._meta.get_field("address")

        assert type(field) == models.CharField
        assert field.verbose_name == "Patient Address"
        assert field.max_length == 255

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 4


class TestExamModel:
    @classmethod
    def setup_class(cls):
        cls.model = ExamModel

    def test_str(self):
        patient = PatientModel()
        exam = ExamModel(patient=patient)

        assert str(exam) == f"Exam for {patient.name}"

    def test_parent_class(self):
        assert issubclass(ExamModel, models.Model)

    def test_meta_verbose_name(self):
        assert self.model._meta.verbose_name == "Exam"

    def test_meta_verbose_name_plural(self):
        assert self.model._meta.verbose_name_plural == "Exams"

    def test_professionals_name_field(self):
        field = self.model._meta.get_field("professionals_name")

        assert type(field) == models.CharField
        assert field.verbose_name == "Professional's Name"
        assert field.max_length == 150

    def test_registration_date_field(self):
        field = self.model._meta.get_field("registration_date")

        assert type(field) == models.DateTimeField
        assert field.verbose_name == "Registration Date"
        assert field.default == timezone.now

    def test_weight_field(self):
        field = self.model._meta.get_field("weight")

        assert type(field) == models.FloatField
        assert field.verbose_name == "Patient Weight"

    def test_height_field(self):
        field = self.model._meta.get_field("height")

        assert type(field) == models.FloatField
        assert field.verbose_name == "Patient Height"

    def test_patient_field(self):
        field = self.model._meta.get_field("patient")

        assert type(field) == models.ForeignKey
        assert field.related_model == PatientModel
        assert field.verbose_name == "Patient"
        assert field.remote_field.related_name == "patient"
        assert field.remote_field.on_delete.__name__ == "CASCADE"

    def test_length_fields(self):
        assert len(self.model._meta.fields) == 6
