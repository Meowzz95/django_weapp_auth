from django.conf.urls import url
from weapp_auth import views

urlpatterns = [
    url(r'^wechatLogin/', views.WeChatLoginApiView.as_view()),
    url(r'^wechatUpdateUserInfo/', views.WeChatUpdateUserInfoApiView.as_view()),
]

