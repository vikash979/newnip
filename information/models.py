from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from django.conf import settings
from datetime import date, datetime
from acknowledge.models import parent_menu


class information_menu(models.Model):
    info_nav = models.ForeignKey(parent_menu,null=True, related_name ="info_menu" ,limit_choices_to={'id': 3}, blank=True, on_delete=models.SET_NULL)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    menu_name =  models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.menu_name
