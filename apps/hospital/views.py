from rest_framework import viewsets

from apps.hospital.models import PatientModel, ExamModel
from apps.hospital.serializers import PatientSerializer, ExamSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = PatientModel.objects.all()
    serializer_class = PatientSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = ExamModel.objects.all()
    serializer_class = ExamSerializer
