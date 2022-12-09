from core_api import router
from .views import PatientViewSet, ExamViewSet

app_name = "apps.hospital"

router.register(r"patient", PatientViewSet, basename=app_name)
router.register(r"exam", ExamViewSet, basename=app_name)
