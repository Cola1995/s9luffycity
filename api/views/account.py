# by luffycity.com
from  rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
import uuid
class authView(APIView):

    def post(self,request,*args,**kwargs):
        # print(request.data)

        ret = {"code":1000}
        user = request.data.get("username")
        pwd  = request.data.get("password")
        print(user)
        user_obj = UserInfo.objects.filter(user= user,pwd=pwd).first()
        if not user_obj:
            ret["code"] = 1001
            ret["error"] = "用户名或密码错误"
        else:
            uid = str(uuid.uuid4())
            UserToken.objects.update_or_create(user = user_obj,defaults = {"token":uid})
            ret["token"] = uid

        return Response(ret)
