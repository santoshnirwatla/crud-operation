from django.contrib import admin
from omesapp.models import Employee

# Register your models here.
class Employe_details(admin.ModelAdmin):
    list_display =['firstname','lastname','dept','salary','mobile','add']

admin.site.register(Employee,Employe_details)