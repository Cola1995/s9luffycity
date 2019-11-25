from api import models
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet,ViewSetMixin



class CourseSerializers(serializers.ModelSerializer):
    """
    课程序列化类
    """
    level = serializers.CharField(source="get_level_display")
    class Meta:
        model = models.Course
        fields = ["id","name","course_img","level"]

class CourseDetailSerializers(serializers.ModelSerializer):
    """
    课程详细序列化类
    """

    # source 可以解决onetoone/forken/choices
    title = serializers.CharField(source='course.name')  # 取关联表数据
    img  = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source="course.get_level_display")  # 取choies 使用get_字段名_display

    # source 多对多写法
    recommends = serializers.SerializerMethodField() #
    # chapter = serializers.SerializerMethodField()  # 章节
    class Meta:
        model = models.CourseDetail

        fields = ["id","why_study","course_slogan","title","img","level","recommends"]
        # depth = 3

    # 取多对多字段
    def get_recommends(self,obj):
        queryset = obj.recommend_courses.all()
        return [{"id":row.id,"title":row.title} for row in queryset]

    # def get_chapter(self,obj):
    #     """
    #     通过课程详细表找课程查找章节
    #     :param obj:
    #     :return:
    #     """
    #     queryset = obj.course.chapter_set.all()
    #     return [{"id": row.id, "name": row.name} for row in queryset]
class CourseSubCategorySerializers(serializers.ModelSerializer):
    """课程子类序列化类"""
    class Meta:
        model = models.CourseSubCategory
        fields = ["name","id"]