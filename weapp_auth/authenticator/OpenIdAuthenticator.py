from django.utils.timezone import now

from rest_framework import authentication, exceptions
import logging

from weapp_auth.models import WeappUser

logger=logging.getLogger(__name__)
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class OpenIdAuthenticator(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        logger.info("OpenId Authenticator token = "+str(token))
        if not token:
            return None

        weapp_user = WeappUser.objects.filter(token=token).first()
        if not weapp_user:
            raise exceptions.AuthenticationFailed('Authentication failed, no such user')
        user=weapp_user.user
        # if user.is_staff:
        #     raise exceptions.AuthenticationFailed('Authentication failed, not admin authenticator')

        user.last_login=now()
        logger.info("user {} last login {} updated".format(user.username,user.last_login))


        return (user, token)
