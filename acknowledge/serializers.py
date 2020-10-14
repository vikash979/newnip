from rest_framework import serializers
from application.models import application_parent_menu
from information.models import information_menu

from othersites.models import otherSites_menu

from .models import (ack_NavyInstructionname, ack_Navyname,graphDetail, ack_publicationname, 
  ack_Standardsname,graphDetailUsed,  ack_guidelinesname , BRsmenu, ack_subGuidelinesmenu, 
  ack_subpublicationmenu,acknoledge_menu,parent_menu,Ack_submenu,ack_policyname,ack_policypolicyfile, ack_subStandardsmenu, 
  ack_subNavy_Orderssmenu, ack_subNavy_Instructionssmenu ,ack_subNHQe_Librarylinesmenu, ack_subMenuPolicyFile, KnowledgeUser)

class DynamicFieldsSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		fields = kwargs.pop('fields', set())
		super().__init__(*args, **kwargs)

		if fields and '__all__' not in fields:
			all_fields = set(self.fields.keys())
			print("vvvvvvhhhhhhhhhhhhhhhhhhhhhhhhhhv", all_fields)
			for not_requested in all_fields - set(fields):
				self.fields.pop(not_requested)

class application_menuSerializer(DynamicFieldsSerializer):
	class Meta:
		model = application_parent_menu
		fields = ['menu_name','id']


class informationSerializer(DynamicFieldsSerializer):
	class Meta:
		model = information_menu
		fields = ['menu_name', 'id']

####################Othersites##########

class otherMenuSerializer(DynamicFieldsSerializer):
	class Meta:
		model = otherSites_menu
		fields = ['menu_name', 'id']




###############################Acknowledge ############################
class AckenowledgepolicypolicyfileSerializer(DynamicFieldsSerializer):
	class Meta:
		model = ack_policypolicyfile
		fields = '__all__'

class AckenowledgePolicynameSerializer(DynamicFieldsSerializer):
	ask_policyfile = AckenowledgepolicypolicyfileSerializer(many=True)
	class Meta:
		model = ack_policyname
		fields = '__all__'



class AckenowledgeNavyOrdersSerializer(DynamicFieldsSerializer):
	class Meta:
		model = ack_Navyname
		fields = '__all__'







class AckguideLineSerializer(DynamicFieldsSerializer):
	class Meta:
		model = ack_guidelinesname
		fields = '__all__'


class AckStandardSerializer(DynamicFieldsSerializer):
	class Meta:
		model = ack_Standardsname
		fields = '__all__'



class ack_subMenuPolicyFileSubmenuSerializer(DynamicFieldsSerializer):

	class Meta:
		model = ack_subMenuPolicyFile
		fields = '__all__'

class policyUserSerializer(DynamicFieldsSerializer):
	class Meta:
		model = KnowledgeUser
		fields = '__all__'

class AckenowledgeSubmenuSerializer(DynamicFieldsSerializer):
	ack_submenu_children = ack_subMenuPolicyFileSubmenuSerializer(many=True)

	# file_data = serializers.SerializerMethodField()
	policy_dt = serializers.SerializerMethodField()
	# policypie_count = serializers.SerializerMethodField()
	menu_user = policyUserSerializer(many=True)
	

	class Meta:
		model= Ack_submenu
		fields= '__all__'

	def get_policy_dt(self,obj):
		menu = Ack_submenu.objects.filter(parent_ob=obj.id)
		return AckenowledgeSubmenuSerializer(menu, many=True).data
		

class AckenowledgePublicationMenuSerializer(DynamicFieldsSerializer):

	class Meta:
		model = ack_publicationname
		fields = '__all__'


class AckenowledgepublicationSubmenuSerializer(DynamicFieldsSerializer):

	ack_publication_children = AckenowledgePublicationMenuSerializer(many=True)
	public_dt = serializers.SerializerMethodField()


	class Meta:
		model= ack_subpublicationmenu
		fields= '__all__'


	def get_public_dt(self,obj):
		menu = ack_subpublicationmenu.objects.filter(parent_ob=obj.id)
		return AckenowledgepublicationSubmenuSerializer(menu, many=True).data





class AckenowledgeGuidelinesSubmenuSerializer(DynamicFieldsSerializer):
	guidelinesMenues = AckguideLineSerializer(many=True)
	public_dt = serializers.SerializerMethodField()
	class Meta:
		model= ack_subGuidelinesmenu
		fields= '__all__'

	def get_public_dt(self,obj):
		menu = ack_subGuidelinesmenu.objects.filter(parent_ob=obj.id)
		return AckenowledgeGuidelinesSubmenuSerializer(menu, many=True).data

class AckenowledgeStandardsSerializer(serializers.ModelSerializer):
	#standards_name = AckStandardSerializer(many=True)
	class Meta:
		model= ack_subStandardsmenu
		fields= '__all__'


class Ack_subNavy_OrderssmenuSerializer(DynamicFieldsSerializer):
	navyOrders_name = AckenowledgeNavyOrdersSerializer(many=True)
	public_dt = serializers.SerializerMethodField()
	class Meta:
		model= ack_subNavy_Orderssmenu
		fields= '__all__'

	def get_public_dt(self,obj):
		menu = ack_subNavy_Orderssmenu.objects.filter(parent_ob=obj.id)
		return Ack_subNavy_OrderssmenuSerializer(menu, many=True).data


class AckenowledgeNavyInstructionSerializer(DynamicFieldsSerializer):
	class Meta:
		model = ack_NavyInstructionname
		fields = '__all__'

class AckNavyInstmenuSerializer(DynamicFieldsSerializer):
	navyinstruction_name = AckenowledgeNavyInstructionSerializer(many=True)
	public_dt = serializers.SerializerMethodField()


	class Meta:
		model= ack_subNavy_Instructionssmenu
		fields= '__all__'

	def get_public_dt(self,obj):
		menu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob=obj.id)
		return AckNavyInstmenuSerializer(menu, many=True).data



class AckLibrarySerializer(DynamicFieldsSerializer):
	class Meta:
		model= ack_subNHQe_Librarylinesmenu
		fields= '__all__'


class BRsmenuSerializer(DynamicFieldsSerializer):
	class Meta:
		model= BRsmenu
		fields= '__all__'


class publicationMenuSerializer(DynamicFieldsSerializer):
	class Meta:
		models = ack_publicationname
		fields = '__all__'


class graphDetailUsedSerializer(DynamicFieldsSerializer):
	class Meta:
		model = graphDetailUsed
		fields = ['menu_detail']

class graphDetailUserSerializer(DynamicFieldsSerializer):
	graph_detail = graphDetailUsedSerializer(many=True)


	class Meta:
		model = graphDetail
		fields = ['menu_detail','graph_detail']


class  AckenowledgeSerializer(DynamicFieldsSerializer):
	#ask_subpublicationmenues = AckenowledgePublicationSerializer(many=True)
	# ask_submenues = AckenowledgeSubmenuSerializer(many=True)
	ascsubmenu_count = serializers.SerializerMethodField()
	# ask_subpublicationmenues = AckenowledgepublicationSubmenuSerializer(many=True)
	# ascpublicationsubmenu_count = serializers.SerializerMethodField()
	# ask_subguidelinesmenues = AckenowledgeGuidelinesSubmenuSerializer(many=True)
	# ascguideleinessubmenu_count = serializers.SerializerMethodField()
	# standards = serializers.SerializerMethodField()
	# ask_substandardsmenues = AckenowledgeStandardsSerializer(many=True)
	# ask_subnavy_ordersmenues = Ack_subNavy_OrderssmenuSerializer(many=True)
	# navy_ordersCount = serializers.SerializerMethodField()
	# navy_ordersCountall = serializers.SerializerMethodField()
	# ask_subnavy_instructionmenues = AckNavyInstmenuSerializer(many=True)
	# navyInstrctionCount = serializers.SerializerMethodField()
	# navyInstrctionCountall = serializers.SerializerMethodField()
	# ask_subnohqsmenues = AckLibrarySerializer(many=True)
	# ask_libCount = serializers.SerializerMethodField()
	# brsmenues = BRsmenuSerializer(many=True)
	# brsCount = serializers.SerializerMethodField()
	#
	#policy_file = serializers.SerializerMethodField()
	pie_count = serializers.SerializerMethodField()
	ask_submenudetail = graphDetailUserSerializer(many=True)



	class Meta:
		model = acknoledge_menu
		fields = ['menu_name','id','ask_submenudetail','ascsubmenu_count','pie_count']


	def get_pie_count(self,obj):
		if obj.id ==1:
			count = ack_subMenuPolicyFile.objects.all().count()
		if obj.id ==2:
			count = ack_publicationname.objects.all().count()
		if obj.id ==3:
			count = ack_Navyname.objects.all().count()
		if obj.id ==4:
			count = ack_NavyInstructionname.objects.all().count()
		if obj.id ==5:
			count = ack_guidelinesname.objects.all().count()
		if obj.id ==6:
			count = ack_Standardsname.objects.all().count()
		return count



	def get_ascsubmenu_count(self,obj):

		#submenu = ack_submenu.objects.filter(parent_id=obj.id).order_by("-id")[:4]
		submenu  = Ack_submenu.objects.all().order_by("-id")[:4]
		#return AckenowledgeSubmenuSerializer(submenu,many=True).data
		return AckenowledgeSubmenuSerializer(submenu,many=True).data
	


class ParentSerializer(DynamicFieldsSerializer):
	navMenu = serializers.SerializerMethodField()
	#navMenues = serializers.SerializerMethodField()
	class Meta:
		model = parent_menu
		fields = ['menu_name','id', 'navMenu','menu_url']


	def get_navMenu(self,obj):
		if obj.id == 1:
			appnavmenu  = application_parent_menu.objects.all()
			serializer =  application_menuSerializer(appnavmenu,many=True)
			return serializer.data
		if obj.id == 2:
			appnavmenu  = acknoledge_menu.objects.all().order_by('id')
			serializer =  AckenowledgeSerializer(appnavmenu,many=True)
		if obj.id == 3:
			appnavmenu  = information_menu.objects.all()
			serializer =  informationSerializer(appnavmenu,many=True)
		# if obj.id == 4:
		# 	appnavmenu  = otherSites_menu.objects.all()
		# 	serializer =  otherMenuSerializer(appnavmenu,many=True)
		return serializer.data
