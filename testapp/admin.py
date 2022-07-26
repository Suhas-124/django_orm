from django.contrib import admin
from testapp.models import Employee,ProxyEmployee,ProxyEmployee1

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddrs']

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddrs']

class ProxyEmployeeAdmin1(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddrs']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee1,ProxyEmployeeAdmin1)



