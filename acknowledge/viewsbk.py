from django.db import models
from django.conf import settings
from .models import (ack_subStandardsmenu, ack_Navyname, ack_subNavy_Orderssmenu,
 ack_subGuidelinesmenu,ack_Standardsname,  graphDetail,ack_guidelinesname,
  ack_subMenuPolicyFile, ack_subNavy_Instructionssmenu,graphDetailUsed,
   ack_subpublicationmenu, ack_publicationname, acknoledge_menu,parent_menu,
   ack_submenu, ack_policyname, ack_policypolicyfile,
    ack_NavyInstructionname, KnowledgeUser, PublicationUser, InstructionUser, NavyUser, GuideLinesUser, StandardUser)
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
#from users.models import CustomUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from application.views import BasicPagination
from rest_framework.pagination import PageNumberPagination
from application.views import PaginationHandlerMixin, BasicPagination
from django.http import Http404,HttpResponse
from rest_framework import status
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView , View
from django.shortcuts import render, redirect
from users.models import User

pagination_ob = settings.PAGINATION_SIZE


class ParentViewApi(APIView):

	def get_object(self):
		try:
			return parent_menu.objects.all()
		except parent_menu.DoesNotExist:
			return Http404

	def get(self, request):
		parent_obj = self.get_object()
		serializer = serializers.ParentSerializer(parent_obj,many=True)
		return Response(serializer.data)




class publicationfileApi(APIView):
    def get(self,request):
        if request.GET['menu'] == 'Policy':

            knowmenu = ack_subMenuPolicyFile.objects.all().order_by("-id")[:4]
            serializer = serializers.ack_subMenuPolicyFileSubmenuSerializer(knowmenu, many=True)
            know_Count = ack_subMenuPolicyFile.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_Count



        if request.GET['menu'] == 'Publication':
            knowpubmenu = ack_publicationname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgePublicationMenuSerializer(knowpubmenu, many=True)
            know_Count = ack_publicationname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_Count
        if request.GET['menu'] == 'Navy Orders':
            knowordermenu = ack_Navyname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgeNavyOrdersSerializer(knowordermenu, many=True)
            know_Count = ack_Navyname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_Count
        if request.GET['menu'] == 'Navy Instruction':
            knowInstructionmenu = ack_NavyInstructionname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgeNavyInstructionSerializer(knowInstructionmenu, many=True)
            know_Count = ack_NavyInstructionname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_Count
        if request.GET['menu'] == 'GuideLines':
          knowInstructionmenu = ack_guidelinesname.objects.all().order_by("-id")[:4]
          serializer = serializers.AckguideLineSerializer(knowInstructionmenu, many=True)
          know_Count = ack_guidelinesname.objects.all().count()
          data  =  {"data":serializer.data}
          data['count'] = know_Count
        if request.GET['menu'] == 'Standards':
          knowInstructionmenu = ack_Standardsname.objects.all().order_by("-id")[:4]
          serializer = serializers.AckStandardSerializer(knowInstructionmenu, many=True)
          know_Count = ack_Standardsname.objects.all().count()
          data  =  {"data":serializer.data}
          data['count'] = know_Count
        return Response(data)

class policyViewobjApi(APIView):
	def get_object(self):
		try:
			return ack_policyname.objects.all()

		except ack_policyname.DoesNotExist:
			return Http404
	def get(self,request,id,sm_id):

		policy_name =  ack_policyname.objects.filter(parent_ob_id=id)
		serializer = serializers.AckenowledgePolicynameSerializer(policy_name,many=True)
		return Response(serializer.data)


class knowledgeGraphApi(APIView):
	def get_all_children(self,menubar,id=None,lists=None):
		if id == None:
			policy_name =  menubar.objects.filter(parent_ob_id=None).values('id')
		else:
			# print("::!!!!", id)
			policy_name =  menubar.objects.filter(id=id).values('id')
			# print("**********************", policy_name)

		# policy_name =  menubar.objects.filter(parent_ob_id=None).values('id')
		
		for pli in policy_name:
			if lists is None:
				polilistss=[]
				#print("############",)
				polilistss.append(pli['id'])
			else:
				polilistss= lists
				polilistss.append(pli['id'])

			policy_data =  menubar.objects.filter(parent_ob_id=pli['id'] ).values('id')
			print("$$$$$$$$$$$$", polilistss)
			for policy_obj in policy_data:

				self.get_all_children(menubar, policy_obj['id'], lists=polilistss)
			
		return polilistss



	def get(self,request, format=None):
		
		if request.GET.get('menubar')  == 'Policy':
			policy_name =  ack_submenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
			serializer = serializers.AckenowledgeSubmenuSerializer(policy_name, many=True)
			policy =[]
			policyId =  self.get_all_children(ack_submenu)
			# print("&&&&&&&&&&&&&&&&&", policy_name)
		return Response(serializer.data)
from django.http import JsonResponse

def get_all_children(id,menubar,lists=None):
	policy_name =  menubar.objects.filter(id=id ).values()
	for pli in policy_name:
			if lists is None:
				polilistss=[]
				#print("############",)
				polilistss.append(pli['id'])
			else:
				polilistss= lists
				polilistss.append(pli['id'])
			policy_data =  menubar.objects.filter(parent_ob_id=pli['id'] ).values('id')
			for policy_obj in policy_data:
				get_all_children(policy_obj['id'],menubar,lists=polilistss)
				# print("£££££££££££££££££", policy_obj )
	return polilistss




def graphCount(request):
	print("///////////////////////////////uuu///////", request.GET.get('menubar'))
	policyobjId = []
	policyobjIds = []
	barobjIds = []
	if request.GET.get('menubar')  == 'Policy':
		policy_name =  ack_submenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_submenu )
			graph_count = ack_subMenuPolicyFile.objects.filter(parent_ob__in=policyId).count()
			graph_record = {x['submenu_name']: graph_count}
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			bargraph_count = KnowledgeUser.objects.filter(user__in=policyId).count()

			# Bra Graph
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)

			policyobjId.append(graph_records)
	if request.GET.get('menubar')  == 'Publication':
		policy_name =  ack_subpublicationmenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_subpublicationmenu )
			graph_count = ack_publicationname.objects.filter(parent_ob__in=policyId).count()
			bargraph_count = PublicationUser.objects.filter(user__in=policyId).count()
			graph_record = {x['submenu_name']: graph_count}
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)
			policyobjId.append(graph_records)
	if request.GET.get('menubar')  == 'Navy Instruction':

		policy_name =  ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_subNavy_Instructionssmenu )
			graph_count = ack_NavyInstructionname.objects.filter(parent_ob__in=policyId).count()
			bargraph_count = InstructionUser.objects.filter(user__in=policyId).count()
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)
			graph_record = {x['submenu_name']: graph_count}
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			policyobjId.append(graph_records)
	if request.GET.get('menubar')  == 'GuideLines':
		policy_name =  ack_subGuidelinesmenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_subGuidelinesmenu )
			graph_count = ack_guidelinesname.objects.filter(parent_ob__in=policyId).count()
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			policyobjId.append(graph_records)
			bargraph_count = GuideLinesUser.objects.filter(user__in=policyId).count()
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)
	if request.GET.get('menubar')  == 'Standards':
		policy_name =  ack_subStandardsmenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_subStandardsmenu )
			graph_count = ack_Standardsname.objects.filter(parent_ob__in=policyId).count()
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			policyobjId.append(graph_records)

			bargraph_count = StandardUser.objects.filter(user__in=policyId).count()
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)


	if request.GET.get('menubar')  == 'Navy Orders':
		policy_name =  ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		for x in policy_name:
			policyId  =  get_all_children(x['id'], ack_subNavy_Orderssmenu )
			graph_count = ack_Navyname.objects.filter(parent_ob__in=policyId).count()
			graph_records = {"name": x['submenu_name'], "y": graph_count}
			policyobjId.append(graph_records)

			bargraph_count = NavyUser.objects.filter(user__in=policyId).count()
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)
	data  = ({"asd":policyobjId,"barhraph": barobjIds,"knowledgetype" : request.GET.get('menubar')})

	return JsonResponse(data, safe=False)

class policyViewApi(APIView, PaginationHandlerMixin):

	def get_object(self):
		try:
			return ack_policyname.objects.all()

		except ack_policyname.DoesNotExist:
			return Http404

	def sub_child(self,id,lists=None):

		policy = ack_publicationname.objects.filter(parent_ob_id__in=id).count()

	def get_all_children(self,id,menubar,lists=None):

		policy_name =  menubar.objects.filter(id=id ).values()


		for pli in policy_name:
			if lists is None:
				polilistss=[]
				#print("############",)
				polilistss.append(pli['id'])
			else:
				polilistss= lists
				polilistss.append(pli['id'])
			#policy_names =  menubar.objects.filter(parent_ob_id=pli['id'] ).values()
			policy_data =  menubar.objects.filter(parent_ob_id=pli['id'] ).values('id')


			for policy_obj in policy_data:

				self.get_all_children(policy_obj['id'],menubar,lists=polilistss)






		return polilistss



	def get(self,request, id,format=None):
		#print("###",request.GET.get('menubar'))
		if request.GET.get('menubar') == 'Publications':
			policy_name =  ack_subpublicationmenu.objects.filter(parent_id=id).values()
			policy_Id = self.get_all_children(id,ack_subpublicationmenu)
			subpolicy = self.sub_child(policy_Id)
			paginator = LimitOffsetPagination()
			print


			#policy_name =  ack_subpublicationmenu.objects.filter(id__in=policy_Id)
			policy_name =  ack_subpublicationmenu.objects.filter(parent_ob_id__in=id)


			serializer = serializers.AckenowledgepublicationSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_publicationname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgePublicationMenuSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data


		elif request.GET.get('menubar') == 'Navy Instructions':
			policy_Id = self.get_all_children(id,ack_subNavy_Instructionssmenu)
			policy_name =  ack_subNavy_Instructionssmenu.objects.filter(id__in=policy_Id)
			serializer = serializers.AckNavyInstmenuSerializer(policy_name,many=True)

		elif request.GET.get('menubar') == 'Guidelines':
			policy_Id = self.get_all_children(id,ack_subGuidelinesmenu)
			#policy_name =  ack_subGuidelinesmenu.objects.filter(id__in=policy_Id) #ack_guidelinesname
			policy_name =  ack_subGuidelinesmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_guidelinesname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckguideLineSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data



		elif request.GET.get('menubar') == 'Navy Orders':
			policy_Id = self.get_all_children(id,ack_subNavy_Orderssmenu)
			#policy_name =  ack_subGuidelinesmenu.objects.filter(id__in=policy_Id) #ack_guidelinesname
			policy_name =  ack_subNavy_Orderssmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Navyname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgeNavyOrdersSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data


		elif request.GET.get('menubar') == 'Standards':
			policy_Id = self.get_all_children(id,ack_subStandardsmenu)
			#policy_name =  ack_subStandardsmenu.objects.filter(id__in=policy_Id)
			policy_name =  ack_subStandardsmenu.objects.filter(parent_ob_id__in=id)
			serializer = serializers.AckenowledgeStandardsSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Standardsname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckStandardSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data

		else:



			policy_name =  ack_submenu.objects.filter(id=id ).values()# | ack_submenu.objects.filter(parent_ob_id=id ).values()
			policy =[]

			policyId =  self.get_all_children(id,ack_submenu)
			
			policy_name =  ack_submenu.objects.filter(id__in=policyId )
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=id)
			#print("::::::::::::::",policy_file.values())


			
			serializer = serializers.AckenowledgeSubmenuSerializer(policy_name,many=True)
			data_record = {"policy": serializer.data}
			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
			
			data_record['obj']  = data_obj.data

			#print("@@@@@@@@@@@@@@@@@@@@:::::::::::::::",data_record)


		return Response(data_record)

class policynewViewApi(APIView):
	def get(self,request,id,sm_id):

		policy_name =  ack_policyname.objects.filter(parent_ob_id=id,folder_type=2)

		serializer =serializers.AckenowledgePolicynameSerializer(policy_name,many=True)


		return Response(serializer.data)


class AcknowledgeAPI(APIView):
    def get_object(self):
        try:
            return acknoledge_menu.objects.all().order_by('id')
        except acknoledge_menu.DoesNotExist:
            return Http404
    def get(self, request,  format=None):
        ack_menu = self.get_object()
        serializer = serializers.AckenowledgeSerializer(ack_menu,many=True)
        data  = serializer.data
        return Response(serializer.data)


class AxknowledgePublicAPI(APIView):
	def get_object(self):
		try:
			return ack_subpublicationmenu.objects.all()

		except ack_subpublicationmenu.DoesNotExist:
			return Http404
	def get(self, request,  format=None):
		ack_menu = self.get_object()
		serializer = serializers.AckenowledgepublicationSubmenuSerializer(ack_menu,many=True)
		return Response(serializer.data)

from rest_framework.pagination import LimitOffsetPagination
class knowledgeMat(APIView):

	def get(self, request):
		# print("!!!!!!!!!!!!", request.GET.get('menubar') )
		if request.GET.get('menubar') == 'Policy':
			submenu = ack_submenu.objects.filter(parent_ob_id=None,folder_type=2, status=2, file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgeSubmenuSerializer(submenu,many=True)			
			if request.GET.get('page_number')==None:
				page_number = 1
			else:
				page_number = int(request.GET.get('page_number'))
			
			# page_number = self.request.query_params.get('page_number ', 1)
			page_size = self.request.query_params.get('page_size ', 5)
			paginator = Paginator(submenu , page_size)

			try:
				users = paginator.page(page_number)
			except PageNotAnInteger :
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			serializer = serializers.AckenowledgeSubmenuSerializer(users , many=True, context={'request':request})
			print(";;;;;;;;;;;;;;;;;;;;;;;;;;;", request.GET.get('menubar'))
			data_record = {"policy": serializer.data}
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
			data_record['obj']  = data_obj.data


		if request.GET.get('menubar') == 'Publication':
			submenu = ack_subpublicationmenu.objects.filter(parent_ob_id=None,folder_type=2,  file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgepublicationSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_publicationname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgePublicationMenuSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
		if request.GET.get('menubar') == 'Navy Orders':
			submenu = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None,folder_type=2,  file_type=request.GET.get('file_type'))
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Navyname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgeNavyOrdersSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
		if request.GET.get('menubar') == 'GuideLines':
			submenu = ack_subGuidelinesmenu.objects.filter(parent_ob_id=None,folder_type=2,  file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_guidelinesname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckguideLineSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
		elif request.GET.get('menubar') == 'Navy Instruction' :
			# print("£££££££££££ssss",id)
			submenu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None,folder_type=2,  file_type=request.GET.get('file_type'))
			serializer = serializers.AckNavyInstmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_NavyInstructionname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgeNavyInstructionSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data

		return Response(data_record)


class AckpolicyAPI(APIView):
	def get(self,request, id):
		print("££££££££££££££", id)
		print(request.GET.get('menubar'))

		if request.GET.get('menubar') == 'Policy':
			submenu = ack_submenu.objects.filter(parent_ob_id=id,folder_type=2, status=2, file_type=request.GET.get('file_type'))

			serializer = serializers.AckenowledgeSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=id)
			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
			
			data_record['obj']  = data_obj.data
		# elif request.GET.get('menubar') == 'Navy Instructions':

		# 	submenu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=id,folder_type=2, file_type=request.GET.get('file_type'))
		# 	serializer = serializers.AckNavyInstmenuSerializer(submenu,many=True)

		# elif request.GET.get('menubar') == 'Guidelines':

		# 	submenu = ack_subGuidelinesmenu.objects.filter(parent_ob_id=id,folder_type=2)
		# 	serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(submenu,many=True)

		elif request.GET.get('menubar') == 'Standards':
			submenu = ack_subStandardsmenu.objects.filter(parent_ob_id=id,folder_type=2, file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgeStandardsSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Standardsname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckStandardSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data

		elif request.GET.get('menubar') == 'Navy Orders':
			submenu = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=id,folder_type=2, file_type=request.GET.get('file_type'))
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Navyname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgeNavyOrdersSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
		elif request.GET.get('menubar') =='GuideLines':
			submenu = ack_subGuidelinesmenu.objects.filter(parent_ob_id=id,folder_type=2, file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_guidelinesname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckguideLineSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
		elif request.GET.get('menubar') == 'Navy Instruction' :
			submenu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=id,folder_type=2, file_type=request.GET.get('file_type'))
			serializer = serializers.AckNavyInstmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_NavyInstructionname.objects.filter(parent_ob_id=id)
			data_obj = serializers.AckenowledgeNavyInstructionSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data
            

		else:
			submenu = ack_subpublicationmenu.objects.filter(parent_ob_id=id, folder_type=2, file_type=request.GET.get('file_type'))
			serializer = serializers.AckenowledgepublicationSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_publicationname.objects.filter(parent_ob_id=id)
			
			data_obj = serializers.AckenowledgePublicationMenuSerializer(policy_file, many=True)
			data_record['obj'] = data_obj.data

		#print(":::::::::",serializer.data) ack_publicationname
		return Response(data_record)

# class AckpolicypubAPI(APIView):

# 	def get(self,request)




class acknowledgeViews(TemplateView):
    template_name = "acknowledge/policy2.html"

    def get_all_child(self, menubar,menutype,mainfile,lists=None):
        policy_name =  menubar.objects.filter(parent_ob_id=None).values('id')
        # print("!", policy_name)
        policylist = []
        for pli in policy_name:
        	# print(menubar,"$$$$$$$$$$$$", pli['id'] )
        	policy_data =  mainfile.objects.filter(parent_ob_id=pli['id'] ).values()
        	for obj in policy_data:
        		policylist.append(obj)
        # print("^^^^^",policylist)
        return policylist
            
            
                
            

    def get(self, request, id=None):
        context_data = {}
        print(request.GET.get('menutype'))
        menu_id = graphDetail.objects.get(menu_detail=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id).id
        graph_obj = graphDetailUsed.objects.create(menu_detail_id=menu_id, menu_user=User.objects.get(username=request.user.username))
        if request.GET.get('menutype') =='Policy' :
            policy_data = ack_submenu.objects.filter(parent_ob_id=None, status=2, file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_submenu.objects.filter(parent_ob_id=None)
            policy_Id = self.get_all_child(ack_submenu,request.GET.get('menutype'),ack_subMenuPolicyFile)
            # pagination_ob = 4

            # paginator = Paginator(policy_data,pagination_ob)
            # if request.GET.get('page')==None:
            # 	page =1
            # else:
            # 	page = int(request.GET.get('page'))
            # try:
            # 	users = paginator.page(page)
            # except PageNotAnInteger:
            # 	users = paginator.page(1)
            # except EmptyPage:
            # 	users = paginator.page(paginator.num_pages)
            # print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::", users)
            
        elif request.GET.get('menutype') =='Publication' :
            policy_data = ack_subpublicationmenu.objects.filter(parent_ob_id=None, file_type=1,parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subpublicationmenu.objects.all().order_by("-id")
            policy_Id = self.get_all_child(ack_subpublicationmenu,request.GET.get('menutype'),ack_publicationname)

        elif request.GET.get('menutype') =='GuideLines' :
            policy_data = ack_subGuidelinesmenu.objects.filter(parent_ob_id=None, file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subGuidelinesmenu.objects.all().order_by("-id")
            policy_Id = self.get_all_child(ack_subGuidelinesmenu,request.GET.get('menutype'),ack_guidelinesname)

        elif request.GET.get('menutype') =='Standards' :
            policy_data = ack_subStandardsmenu.objects.filter(parent_ob_id=None,  file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subStandardsmenu.objects.all().order_by("-id")
            policy_Id = self.get_all_child(ack_subStandardsmenu,request.GET.get('menutype'),ack_Standardsname)

        elif request.GET.get('menutype') == 'Navy Instruction' :
            policy_data = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None, file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subNavy_Instructionssmenu.objects.all().order_by("-id")
            policy_Id = self.get_all_child(ack_subNavy_Instructionssmenu,request.GET.get('menutype'),ack_Standardsname)

        elif request.GET.get('menutype') =='Navy Orders' :
            policy_data = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None, file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subNavy_Orderssmenu.objects.all().order_by("-id")
            policy_Id = self.get_all_child(ack_subNavy_Orderssmenu,request.GET.get('menutype'),ack_Navyname)

        else:
            policy_obj = ack_policyname.objects.all().values().order_by("-id")

        paginator = Paginator(policy_data,pagination_ob)
        if request.GET.get('page')==None:
            page = 1
        else:
            page = int(request.GET.get('page'))
        try:
            users = paginator.page(page)
        except PageNotAnInteger :
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        context_data['policy'] = users
        program_numpages = paginator.num_pages
        program_numpages = program_numpages+1
        context_data['PAGINATION_COUNT'] = range(1,program_numpages)
        context_data['sub_menu'] = users
        context_data['menu_bar'] = request.GET.get('menutype')
        context_data['maneu_typeId'] = request.GET.get('mainId')
        return render(request, self.template_name, context_data)



class policyViews(TemplateView):
	def get(self, request, drink_name,string_name):
		template_name = string_name
		context_data = {}
		return render(request, template_name, context_data)


class ack_menudetail(TemplateView):
	template_name = "acknowledge/publication_menu2.html"
	def get(self, request, id=None):
		context_data = {}
		ack_menu = acknoledge_menu.objects.all().values()
		menu_obj = []
		menu_count = []
		for menu in ack_menu:

			menu_obj.append(menu['menu_name'])
			manu_cnt = ack_submenu.objects.filter(parent_id=menu['id']).count()
			menu_count.append(manu_cnt)

		context_data['data'] = menu_obj
		context_data['labels'] = menu_count



		return render(request, self.template_name, context_data)
