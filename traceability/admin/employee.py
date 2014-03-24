from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from traceability.models.employee import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
