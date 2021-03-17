from django.contrib import admin

# Register your models here.
from myapp.models import Task

admin.site.register(Task)