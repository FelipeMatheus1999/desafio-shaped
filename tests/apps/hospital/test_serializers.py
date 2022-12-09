from rest_framework import serializers

from apps.hospital.models import PatientModel, ExamModel
from apps.hospital.serializers import PatientSerializer, ExamSerializer


class TestPatientSerializer:
    @classmethod
    def setup(cls):
        cls.serializer = PatientSerializer

    def test_parent_class(self):
        assert issubclass(self.serializer, serializers.ModelSerializer)

    def test_meta_model(self):
        assert self.serializer.Meta.model == PatientModel

    def test_meta_fields(self):
        assert self.serializer.Meta.fields == "__all__"


class TestExamSerializer:
    @classmethod
    def setup(cls):
        cls.serializer = ExamSerializer

    def test_parent_class(self):
        assert issubclass(self.serializer, serializers.ModelSerializer)

    def test_meta_model(self):
        assert self.serializer.Meta.model == ExamModel

    def test_meta_fields(self):
        assert self.serializer.Meta.fields == "__all__"

    def test_meta_extras_fields(self):
        assert self.serializer.Meta.extra_kwargs == {
            "registration_date": {"read_only": True}
        }

