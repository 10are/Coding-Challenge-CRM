from crm.models import *
from .serializers import *
from .views import *
from rest_framework import serializers

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class departmentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Department
        fields = '__all__'

class titlehistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleHistory
        fields = '__all__'