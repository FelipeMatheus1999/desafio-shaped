from apps.hospital.serializers import PatientSerializer, ExamSerializer
from apps.hospital.views import PatientViewSet, ExamViewSet


class TestPatientViewSet:
    @classmethod
    def setup(cls):
        cls.view = PatientViewSet

    def test_serializer_class(self):
        assert self.view.serializer_class == PatientSerializer


class TestExamViewSet:
    @classmethod
    def setup(cls):
        cls.view = ExamViewSet

    def test_serializer_class(self):
        assert self.view.serializer_class == ExamSerializer
