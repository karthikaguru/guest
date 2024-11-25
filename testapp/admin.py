from django.contrib import admin
from testapp.models import *
# Register your models here.
class AdminEmployee(admin.ModelAdmin):
    details=['name','images','description']
admin.site.register(Employee,AdminEmployee) 
