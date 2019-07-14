import logging

import requests
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from weapp_auth.authenticator.OpenIdAuthenticator import OpenIdAuthenticator
from weapp_auth.wechat.WeChatUserHelper import handleWechatLogin, handleUpdateUserInfo

logging.basicConfig()
logger = logging.getLogger("weapp_auth_views")
logger.setLevel(logging.DEBUG)

WECHAT_CODE_TO_SESSION_URL="https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code"

class WeChatLoginApiView(APIView):
    authentication_classes = [OpenIdAuthenticator]
    permission_classes = []
    def post(self,request,format=None):
        code=request.data["code"]
        logger.debug(f"wechat login code {code}")
        if not code:
            return Response(status.HTTP_400_BAD_REQUEST)
        url=WECHAT_CODE_TO_SESSION_URL.format(settings.WEAPP_AUTH['APP_ID'],settings.WEAPP_AUTH['APP_SECRET'],code)
        resp=requests.get(url)
        respJson=resp.json()
        unionId=None
        logger.debug(f"resp from wechat server {resp}")
        logger.debug(f"resp json from wechat server {respJson}")
        if "unionid" in respJson:
            unionId=respJson["unionid"]
        token,userId=handleWechatLogin(respJson["openid"],respJson["session_key"],unionId)
        return Response(data={"token":token,"id":userId},status=status.HTTP_200_OK)

class WeChatUpdateUserInfoApiView(APIView):
    authentication_classes = [OpenIdAuthenticator]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        try:
            handleUpdateUserInfo(request.data["encryptedData"],request.data["iv"],request.user)
        except Exception as ex:
            return Response(data={"error":str(ex)},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"id":self.request.user.id}, status=status.HTTP_200_OK)
