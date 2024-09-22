from django.contrib import admin
from .models import Employee,Position,Department,Status

# add to django admin dashboard
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Status)
