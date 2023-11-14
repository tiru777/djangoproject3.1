from django.contrib import admin
from app.models import *

admin.site.register(Department)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Student)
admin.site.register(University)


class EmployeeList(admin.ModelAdmin):
    list_display = ('first_name','email','dob','age')


admin.site.register(Employee,EmployeeList)
