from django.contrib import admin
from .models import Lesson, CustomUser, Grade

# Register your models here.
admin.site.register(Lesson)
admin.site.register(CustomUser)
admin.site.register(Grade)
