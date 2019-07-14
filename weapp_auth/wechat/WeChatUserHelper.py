from django.contrib.auth.models import User
from django.conf import settings
from weapp_auth.wechat.WXBizDataCrypt import WXBizDataCrypt
import uuid
import logging

logger=logging.getLogger(__name__)


def handleWechatLogin(openid:str,session_key:str,unionid:str):
    user=initOrGetUser(openid)
    user.weapp_user.sessionKey=session_key
    user.weapp_user.unionId=unionid
    token=str(uuid.uuid4()).replace('-','')
    user.weapp_user.token=token
    user.save()
    return token,user.id

def handleUpdateUserInfo(encryptedData:str,iv:str,user:User):
    wxCrypt=WXBizDataCrypt(settings.WEAPP_AUTH['APP_ID'],user.weapp_user.sessionKey)
    data=wxCrypt.decrypt(encryptedData,iv)
    if user.username!=data["openId"]:
        logger.error("User mismatch while update user info incoming openid={} db openid={}".format(data["openId"],user.username))
        raise Exception("User mismatch")
    user.weapp_user.nickName=data["nickName"]
    user.weapp_user.gender=data["gender"]
    user.weapp_user.city=data["city"]
    user.weapp_user.province=data["province"]
    user.weapp_user.country=data["country"]
    user.weapp_user.avatarUrl=data["avatarUrl"]
    if "unionId" in data:
        user.weapp_user.unionId=data["unionId"]
    user.weapp_user.language=data["language"]
    user.save()


def initOrGetUser(openid):
    user,created=User.objects.get_or_create(username=openid)
    return user