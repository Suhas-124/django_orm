from django.shortcuts import render
from testapp.models import Employee
from testapp.models import CustomManager
from django.db.models import Avg,Sum,Max,Min,Count

# Create your views here.

def employee_view(request):
    # employees=Employee.objects.all()
    user=request.user
    print(user)
    employees=Employee.objects.get_emp_sorted_by('ename')
    # employees.delete()
    # emcreate=Employee.objects.
    print(employees.count())
    my_dict={'employees':employees,}
    return render(request,'testapp/home.html',my_dict)
