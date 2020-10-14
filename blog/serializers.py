from rest_framework import serializers
from .models import blog_model, Comment
from users.models import User

class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['email']

class  CommentSerializer(serializers.ModelSerializer):
	#tag  = serializers.SerializerMethodField()
	user = CustomUserSerializer(many=False)
	class Meta:
		model = Comment
		fields = '__all__'
		#depth = 1

class  BlogSerializer(serializers.ModelSerializer):
	text = CommentSerializer(many=True)
	class Meta:
		model = blog_model
		fields = '__all__'




	