from django.contrib import admin

# Register your models here.

from .models import Task, SubTask

admin.site.register(Task)
admin.site.register(SubTask)
