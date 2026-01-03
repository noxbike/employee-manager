from django import forms
from .models import Employee

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'position', 'salary', 'hire_date']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input w-full', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input w-full', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'input w-full', 'placeholder': 'Email'}),
            'position': forms.TextInput(attrs={'class': 'input w-full', 'placeholder': 'Position'}),
            'salary': forms.NumberInput(attrs={'class': 'input w-full', 'placeholder': '3000.00'}),
            'hire_date': forms.DateInput(attrs={'class': 'input w-full', 'type': 'date'}),
        }