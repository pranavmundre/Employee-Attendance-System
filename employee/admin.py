from django.contrib import admin

from employee.models import Employee, EmployeeAttendance


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    readonly_fields = ('password', )


class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_present')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeAttendance, EmployeeAttendanceAdmin)
