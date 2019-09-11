from rest_framework.views import APIView
from rest_framework.response import Response

class CourseView(APIView):

    def get(self,request,*args,**kwargs):
        ret = {
            'code':1000,
            'data':[
                      {"id":1,"title":'Python全栈'},
                      {"id":2,"title":'Linux运维'},
                      {"id":3,"title":'金融分析'},
                      {"id":4,"title":'home'},
                    ]
        }
        return Response(ret)