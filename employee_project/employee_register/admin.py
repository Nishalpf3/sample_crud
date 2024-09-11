from django.contrib import admin
from .models import Employee, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'emp_code', 'mobile', 'position')
