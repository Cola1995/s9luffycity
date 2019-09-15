from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from  api.serializers.course import *
# 方式1
# class CourseView(APIView):
#     def get(self,request,*args,**kwargs):
#         """
#         全部课程
#         :param request:
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         # ret = {
#         #
#         #     'code':1000,
#         #     'data':[
#         #               {"id":1,"title":'Python全栈'},
#         #               {"id":2,"title":'Linux运维'},
#         #               {"id":3,"title":'金融分析'},
#         #               {"id":4,"title":'home'},
#         #             ]
#         # }
#         ret = {"code":1000,"data":None}
#
#         try:
#             pk = kwargs.get("pk")
#             if pk :
#                 queryset = models.Course.objects.filter(id=pk).first()
#                 ser = CourseSerializers(instance=queryset, many=False)
#             else:
#                 queryset = models.Course.objects.all()
#                 ser = CourseSerializers(instance=queryset, many=True)
#             ret["data"] = ser.data
#         except :
#             ret["code"] = 1001
#             ret["data"] = "获取课程失败"
#
#         return Response(ret)
# 方式二

class CourseView(ViewSetMixin,APIView): # 注意继承顺序

    def list(self,request,*args,**kwargs):
       ret = {"code":1000,"data":None}
       try:

           queryset = models.Course.objects.all()
           ser = CourseSerializers(instance=queryset,many=True)
           ret["data"] = ser.data
       except:
           ret["code"] = 1001
           ret["data"] = "获取课程失败"
       return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {"code": 1000, "data": None}
        try:
            pk = kwargs.get("pk")
            # queryset = models.Course.objects.filter(id=pk).first()
            queryset = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializers(instance=queryset, many=False)
            ret["data"] = ser.data
        except:

            ret["code"] = 1001
            ret["data"] = "获取课程失败"

        return Response(ret)

