from rest_framework import viewsets
from .models import Employee, Position, Department, Status
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import EmployeeSerializer, PositionSerializer, DepartmentSerializer, StatusSerializer
from .filters import EmployeeFilter, PositionFilter, StatusFilter, DepartmentFilter
from rest_framework.permissions import IsAuthenticated
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    permission_classes = [IsAuthenticated]

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PositionFilter

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DepartmentFilter

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatusFilter
