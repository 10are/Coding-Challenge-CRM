from django.urls import path, include
from rest_framework import routers
from .views import *

routers = routers.DefaultRouter()
routers.register('location', locationViewSet)
routers.register('employee', employeeViewSet)
routers.register('department', departmentViewSet)
routers.register('titlehistory', titlehistoryViewSet)

urlpatterns = [
    path('', include(routers.urls)),

]

