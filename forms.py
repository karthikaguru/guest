from django import forms
from testapp.models import Employee

# Create your models here.
class Employee_forms(forms.ModelForm):
      class Meta:
        model=Employee
        fields='__all__'
        username=forms.CharField(max_length=20)
         #password=forms.PasswordInput()
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }
     