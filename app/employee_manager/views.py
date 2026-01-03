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

def edit_employee(request, employee_id):
    employe = Employee.objects.get(id=employee_id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employe/formulaire.html', {'form': form})

def delete_employee(request, employee_id):
    employe = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        employe.delete()
        return redirect('employee_list')
    return render(request, 'employe/confirm_delete.html', {'employe': employe})