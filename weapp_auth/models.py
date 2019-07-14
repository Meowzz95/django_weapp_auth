from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class WeappUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='weapp_user')
    nickName = models.CharField(max_length=50, blank=True, default='NO NICKNAME')
    avatarUrl = models.TextField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, default='NO CITY')
    province = models.CharField(max_length=100, blank=True, default='NO PROVINCE')
    country = models.CharField(max_length=100, blank=True, default='NO COUNTRY')
    language = models.CharField(max_length=20, blank=True, default='NO LANG')
    unionId = models.CharField(max_length=50, blank=True, null=True)
    sessionKey = models.CharField(max_length=50, blank=True, null=True)
    token = models.CharField(max_length=32, null=True)


@receiver(post_save, sender=User)
def create_weapp_user(sender, instance, created, **kwargs):
    if created:
        WeappUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def update_weapp_user(sender, instance, **kwargs):
    instance.weapp_user.save()
