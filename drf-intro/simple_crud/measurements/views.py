from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, MeasurementSerializer
from .models import Project, Measurement


class ProjectViewSet(ModelViewSet):
    """ViewSet для проекта."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""

    queryset_mes = Measurement.objects.all()
    serializer_class_mes = MeasurementSerializer

