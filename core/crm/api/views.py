from crm.models import *
from rest_framework import viewsets
from .serializers import *



class locationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = locationSerializer



class employeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer



class departmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = departmentSerializer



class titlehistoryViewSet(viewsets.ModelViewSet):
    queryset = TitleHistory.objects.all()
    serializer_class = titlehistorySerializer
