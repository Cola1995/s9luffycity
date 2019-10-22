from django.test import TestCase

# Create your tests here.
# import hmac
# import base64
# from hashlib import sha256
# import hashlib
#
# appsecret = "X9l1reZjEishJf4bGBv7wA41PBj4id6h".encode('utf-8')  # 秘钥
# data = "xxxxx".encode('utf-8')  # 加密数据
# # signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).digest())
# # print(signature)
# #
# # # 获取十六进制加密数据
# # signature = base64.b64encode(hmac.new(appsecret, data, digestmod=sha256).hexdigest())
# # print(signature)
# signature = hmac.new(appsecret, data, digestmod=hashlib.sha256).digest()
# print(signature)
# print(b'[t\x89\xedt\x8c\xef\xba\x93\x9c\xf7o\xd6\x96\xbbh\x80\xc0\xda\x19I\x8e\x19\xc9%!\\\xbb\xfbeo\x14'.decode("utf-8"))

# import  hashlib
# hash = hashlib.sha256("ssss".encode("utf-8"))
# hash.update("X9l1reZjEishJf4bGBv7wA41PBj4id6h".encode("utf-8"))
# print(hash.hexdigest())
import hashlib
import hmac
import base64

# message = bytes("Message").encode('utf-8')
# secret = bytes("X9l1reZjEishJf4bGBv7wA41PBj4id6h").encode('utf-8')
#
# signature = hmac.new("key", message, digestmod=hashlib.sha256).digest();
# signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
# print(signature)

# hmac_sha256 加密函数
appkey = "X9l1reZjEishJf4bGBv7wA41PBj4id6h"
strToSign = "6383"  #需要加密的字符串
signature = hmac.new(bytes(appkey, encoding='utf-8'), bytes(strToSign, encoding='utf-8'), digestmod=hashlib.sha256).digest()
HEX = signature.hex()  #小写
print(HEX)
