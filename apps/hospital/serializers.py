from rest_framework import serializers

from apps.hospital.models import PatientModel, ExamModel


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientModel
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = "__all__"
        extra_kwargs = {
            "registration_date": {"read_only": True}
        }
