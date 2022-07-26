import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_orm.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def populate(n):
    for i in range(n):
        feno=fake.random_element(elements=(600,700,800,900,200,1000,1200,1100))
        fename=fake.random_element(elements=('ramesh','suresh','rakesh','pawan','sushma','sushanth'))
        fesal=fake.random_element(elements=(1000,2000,3000,4000,5000,9999,4566))
        feaddrs=fake.random_element(elements=('bangalore','chennai','kochi','Munnar','E thimmasandr'))
        employee_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddrs=feaddrs)
populate(100)      
