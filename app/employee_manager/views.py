from django.shortcuts import render
from .models import Employee

# Create your views here.

def employee_list(request):
    remployes = Employee.objects.all()
    employes = [{'name': 'mickael', 'email': 'noxbike@gmail.com', 'position': 'developer', 'salary': 50000},]
    return render(request , 'employe/list.html', {'employes': employes})


