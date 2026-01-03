from django.shortcuts import render, redirect
from .models import Employee
from .foms import EmployeForm

# Create your views here.

def employee_list(request):
    employes = Employee.objects.all()
    return render(request , 'employe/list.html', {'employes': employes})

def add_employee(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employe/formulaire.html', {'form': form})