from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(verbose_name="课程名称",max_length=50)
    course_img = models.CharField(verbose_name="课程图片",max_length=100)
    level_choices = (
        (1,"初级"),
        (2,"中级"),
        (3,"高级")
    )
    level = models.IntegerField(verbose_name="等级",choices=level_choices)


class CourseDetail(models.Model):
    why = models.CharField(verbose_name="why",max_length=255)
    course = models.OneToOneField(to=Course)