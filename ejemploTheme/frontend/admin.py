from django.contrib import admin
from .models import Questions, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Questions)