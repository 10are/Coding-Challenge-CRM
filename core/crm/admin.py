from django.contrib import admin

# Register your models here.
from crm.models import *



admin.site.register(Location)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(TitleHistory)
