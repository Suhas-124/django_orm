from weakref import proxy
from django.db import models

# Create your models here.


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-id')

    def get_sal_range(self,esal1,esal2):
        return super().get_queryset().filter(esal__range=(esal1,esal2)).order_by('-eaddrs')

    def get_emp_sorted_by(self,param):
        return super().get_queryset().order_by(param)   

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__range=(1000,3000))

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ename__icontains='s')



class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=80)
    esal=models.IntegerField()
    eaddrs=models.CharField(max_length=80)
    objects=CustomManager()

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee1(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True

