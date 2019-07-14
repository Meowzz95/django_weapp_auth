from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from mi_django_rest_starter import settings
from weapp_auth import views

urlpatterns = [
    url(r'^wechatLogin/', views.WeChatLoginApiView.as_view()),
    url(r'^wechatUpdateUserInfo/', views.WeChatUpdateUserInfoApiView.as_view()),
]

