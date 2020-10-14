from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.conf import settings

from datetime import date, datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)


class blog_model(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)

    blog_heading =  models.CharField(max_length=200)

    blog_count = models.IntegerField(blank=True,default=0)
    #text = models.TextField(blank=True, null=True)
    text = GenericRelation(Comment,related_query_name='blog_model')
