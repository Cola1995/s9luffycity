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

    class Meta:
          verbose_name_plural = "课程表"  #添加表明


    def __str__(self):
        return self.title

class CourseDetail(models.Model):
    """
    课程详细
    """
    why = models.CharField(verbose_name="why",max_length=255)
    slogon = models.CharField(verbose_name="口号",max_length=255)
    course = models.OneToOneField(to=Course)
    recommend_course = models.ManyToManyField(verbose_name="推荐课程",to=Course,related_name="rc") #设置反向查找字段

    class Meta:
        verbose_name_plural = "课程详细表"

    # def __str__(self):
    #     return self.course


class Chapter(models.Model):
    """
    章节
    """
    name = models.CharField(verbose_name="章节名称",max_length=32)
    num = models.IntegerField(verbose_name="章节")
    course = models.ForeignKey(to=Course,verbose_name="所属课程")

    class Meta:
        verbose_name_plural = "课程章节表"
