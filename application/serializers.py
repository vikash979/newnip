from rest_framework import serializers

from .models import application_submenu,application_menu,application_parent_menu, news, policy, publication, wing_commander

class  ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = application_submenu
		fields =['id','submenu_name','menu_id']


class ApplicationmenuSerializer(serializers.ModelSerializer):

	class Meta:
		model = application_submenu
		fields = ('id')

class ApplicationMenuobjSerializer(serializers.ModelSerializer):
	#application_submenu = ApplicationSerializer(many=True)
	class Meta:
		model = application_menu
		#fields = ['id','menu_name','parent','parent_ob','menu_type','parent_ob']
		fields = '__all__'


class ParentMenuerializer(serializers.ModelSerializer):
	#application_menu = ApplicationMenuobjSerializer(many=True)

	application_menu = serializers.SerializerMethodField()
	class Meta:
		model = application_parent_menu
		fields = '__all__'

	def get_application_menu(self,obj):

		hh =application_menu.objects.filter(parent_id=obj.id,menu_type=1,parent_ob_id=None).values()
		return ApplicationMenuobjSerializer(hh,many=True).data



class ApplicationMenuuobjSerializer(serializers.ModelSerializer):
	#application_submenu = ApplicationSerializer(many=True)
	#date_of_birth =  serializers.SerializerMethodField()
	class Meta:
		model = application_menu
		fields = '__all__'

	# def get_date_of_birth(self,obj):
	# 	queryset = application_menu.objects.filter(parent_ob_id=obj['id'])
	# 	#print("################",queryset.values())
	# 	return ApplicationMenuobjSerializer(queryset,many=True)

class NewsMenuuobjSerializer(serializers.ModelSerializer):
	class Meta:
		model = news
		fields = ['news_heading','id']

class PolicyobjSerializer(serializers.ModelSerializer):
	class Meta:
		model = policy
		fields = '__all__'



class ApplicationmenuSerializer(serializers.ModelSerializer):
	class Meta:
		model = application_menu
		fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = publication
		fields = '__all__'



class wing_commanderSerializer(serializers.ModelSerializer):
	class Meta:
		model = wing_commander
		fields = '__all__'
