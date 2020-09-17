from django.contrib import admin
from firstapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'gender', 'cities', 'image', 'email', 'password', 'status']

admin.site.register(Employee, EmployeeAdmin)
