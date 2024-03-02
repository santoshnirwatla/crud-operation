from django import forms
from omesapp.models import Employee

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'