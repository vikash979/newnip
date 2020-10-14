from django.db import models
from django.conf import settings
import random

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from django.conf import settings
from datetime import date, datetime



def code_generator(size=6, chars='abcdefghijklmnopqrst'):
	return ''.join(random.choice(chars) for _ in range(size))

class KirUrl(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	address = models.CharField(max_length=200, blank=True, null=True)

	def save(self,request, *args, **kwargs):
		print("@@@@@@@@@@@@@@@@", request)
		self.name = code_generator()
		super(KirUrl,self).save(*args, **kwargs)
