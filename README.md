#Weapp Auth

Weapp auth is a Django app that helps to handle wechat mini program login and user info updating logic.

Quick start
-----------

1. Add "weapp_auth" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'weapp_auth',
    ]

2. Include the weapp_auth URLconf in your project urls.py like this::

    path('weapp_auth/', include('weapp_auth.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. These two APIs are avaliable! `weapp_auth/wechatLogin/` and `weapp_auth/wechatUpdateUserInfo/`

5. Call these two APIs in your wechat mini app!