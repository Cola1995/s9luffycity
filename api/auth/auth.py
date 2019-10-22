from rest_framework.authentication import BasicAuthentication

from rest_framework.exceptions import AuthenticationFailed
from api.models import *

class luffAuth(BasicAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        obj = UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({"code":1001,"error":"认证失败"})
        return (obj.user.user,obj)