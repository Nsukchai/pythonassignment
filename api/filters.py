from django_filters import FilterSet, filters, CharFilter, NumberFilter
from django.db.models import Q
import django_filters
from .models import Employee, Position, Department, Status

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  
    address = django_filters.CharFilter(lookup_expr='icontains')
    manager = django_filters.BooleanFilter() 
    status = django_filters.NumberFilter(field_name='status__id')  

    class Meta:
        model = Employee
        fields = ['name', 'address', 'manager', 'status']

class PositionFilter(django_filters.FilterSet):
    position_name = django_filters.CharFilter(lookup_expr='icontains')  
    salary = django_filters.NumberFilter(lookup_expr='icontains')  

    class Meta:
        model = Position
        fields = ['position_name', 'salary']

class DepartmentFilter(django_filters.FilterSet):
    department_name = django_filters.CharFilter(lookup_expr='icontains')  
    manager = django_filters.NumberFilter(lookup_expr='icontains')  

    class Meta:
        model = Department
        fields = ['department_name', 'manager']

class StatusFilter(django_filters.FilterSet):
    status_name = django_filters.ChoiceFilter(choices=Status.status_choices)

    class Meta:
        model = Status
        fields = ['status_name']

