from rest_framework import serializers
from application.models import application_parent_menu
from information.models import information_menu
from users.models import User

class userSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'name','role')