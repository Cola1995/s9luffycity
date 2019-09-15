from django.contrib import admin

# Register your models here.
from api import models

admin.site.register(models.Course)
admin.site.register(models.Chapter)
admin.site.register(models.CourseDetail)