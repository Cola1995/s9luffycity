from django.test import TestCase

# Create your tests here.

import hashlib
import hmac
import base64
import  requests
import time
import json
# hmac_sha256 加密函数




def sha256(apiKey,strToSign):
    print(apiKey,strToSign)
    signature = hmac.new(bytes(apiKey, encoding='utf-8'), bytes(strToSign, encoding='utf-8'),
                         digestmod=hashlib.sha256).digest()
    HEX = signature.hex()
    # 小写
    print("小写：" + HEX)
    print("大写："+HEX.upper())

def test(appkey,strToSign):

    signature = base64.b64encode(hmac.new(appkey, strToSign, digestmod=hashlib.sha256).digest())
    print(signature)


def sign_request(method,path,apiSecret):
    r_time = str(time.time()*1000)[0:13]
    method = method.upper()

    enbase64key = base64.b64encode(apiSecret.encode("utf-8")).decode("utf-8")
    message = r_time+method+path
    # print(enbase64key,message)
    api_sign = hmac.new(bytes(enbase64key, encoding='utf-8'), bytes(message, encoding='utf-8'),
                         digestmod=hashlib.sha256).digest()
    HEX = api_sign.hex()

    return (HEX,r_time)

def balances():
    api_sign = sign_request("get", "/api/balances", "/UM0EDr+QhnAMR9yhsynXW1bAa1MxpOt8U+yvPJuHUk=")
    header = {
        "API-KEY": "77f485d5039455b9e7b48657dec357df",
        "API-SIGN": api_sign[0],
        "API-TIMESTAMP": api_sign[1],
        "API-PASSCODE": "qwerdf886."
    }
    res = requests.get("http://116.6.110.50:8007/api/balances", headers=header)
    print(res.text)

    return ""

def batch_place_order(price,increasing,account):

    index = 0
    while(index<account):
        # time.sleep(2)
        index+= 1
        price = float(price)
        price+=increasing
        print(index,price,type(price))
        api_sign = sign_request("post", "/api/orders", "+GXLAUbwd14KXYvr3KK3EACaQRHiFLJkBLJ6wLQbIFw=")
        header = {
            "API-KEY": "92e8cfc65915980630225213631a6e4b",
            "API-SIGN": api_sign[0],
            "API-TIMESTAMP": api_sign[1],
            "API-PASSCODE": "qwerdf886."
        }
        date = {
            "instrumentId": "DTA-BTC",
            "orderType": "LIMIT",
            "postOnly": False,
            "price": str(price)[0:8],
            "selfTradePrevention": "CN",
            "side": "BUY",
            "size": "1134",
            "timeInForce": "GTC"
        }
        res = requests.post("http://116.6.110.50:8007/api/orders",headers = header,data=json.dumps(date))
        print(res.text)
    return  ""


if __name__=="__main__":
    apiKey = "X9l1reZjEishJf4bGBv7wA41PBj4id6h"
    str = "2374320"
    sha256(apiKey,str)

    # accesskey = "92e8cfc65915980630225213631a6e4b"
    # secretkey  = "+GXLAUbwd14KXYvr3KK3EACaQRHiFLJkBLJ6wLQbIFw="
    # batch_place_order(0.0043,0.0001,10000)

