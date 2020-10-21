# from django.db import models
# from django.conf import settings
from django.views.generic import TemplateView , View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404,HttpResponse
from rest_framework import status
from users.models import User
from .models import (ack_subStandardsmenu, ack_Navyname, ack_subNavy_Orderssmenu,
 ack_subGuidelinesmenu, ack_Standardsname,  graphDetail,ack_guidelinesname,
  ack_subMenuPolicyFile, ack_subNavy_Instructionssmenu,graphDetailUsed,
   ack_subpublicationmenu, ack_publicationname, acknoledge_menu,parent_menu,
   Ack_submenu, ack_policyname, ack_policypolicyfile,
    ack_NavyInstructionname, KnowledgeUser, PublicationUser, InstructionUser,
     NavyUser, GuideLinesUser, StandardUser)
from django.contrib.auth import get_user_model
from . import serializers

from django_filters.rest_framework import DjangoFilterBackend
pagination_ob = settings.PAGINATION_SIZE
import os



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
            know_count = ack_subMenuPolicyFile.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_count



        if request.GET['menu'] == 'Publication':
            knowpubmenu = ack_publicationname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgePublicationMenuSerializer(knowpubmenu, many=True)
            know_count = ack_publicationname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_count
        if request.GET['menu'] == 'Navy Orders':
            knowordermenu = ack_Navyname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgeNavyOrdersSerializer(knowordermenu, many=True)
            know_count = ack_Navyname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_count
        if request.GET['menu'] == 'Navy Instruction':
            knowInstructionmenu = ack_NavyInstructionname.objects.all().order_by("-id")[:4]
            serializer = serializers.AckenowledgeNavyInstructionSerializer(knowInstructionmenu, many=True)
            know_count = ack_NavyInstructionname.objects.all().count()
            data  =  {"data":serializer.data}
            data['count'] = know_count
        if request.GET['menu'] == 'GuideLines':
          knowInstructionmenu = ack_guidelinesname.objects.all().order_by("-id")[:4]
          serializer = serializers.AckguideLineSerializer(knowInstructionmenu, many=True)
          know_count = ack_guidelinesname.objects.all().count()
          data  =  {"data":serializer.data}
          data['count'] = know_count
        if request.GET['menu'] == 'Standards':
          knowInstructionmenu = ack_Standardsname.objects.all().order_by("-id")[:4]
          serializer = serializers.AckStandardSerializer(knowInstructionmenu, many=True)
          know_count = ack_Standardsname.objects.all().count()
          data  =  {"data":serializer.data}
          data['count'] = know_count
        return Response(data)

class policyViewobjApi(APIView):
	def get_object(self):
		try:
			return ack_policyname.objects.all()

		except ack_policyname.DoesNotExist:
			return Http404
	def get(self,request,id):

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
			policy_name =  Ack_submenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
			serializer = serializers.AckenowledgeSubmenuSerializer(policy_name, many=True)
			policy =[]
			policyId =  self.get_all_children(Ack_submenu)
			# print("&&&&&&&&&&&&&&&&&", policy_name)
		return Response(serializer.data)


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
	policyobjId = []
	policyobjIds = []
	barobjIds = []
	file_Data = []
	print("---------",request.GET.get('search'))
	if request.GET.get('search')!= None:
		String = request.GET.get('search')
	file_location = os.getcwd()+"/media/"
	if request.GET.get('menubar')  == 'Policy':
		policy_name =  Ack_submenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		
		for x in policy_name:
			policyId  =  get_all_children(x['id'], Ack_submenu )
			graph_count = ack_subMenuPolicyFile.objects.filter(parent_ob__in=policyId).count()
			file_name = ack_publicationname.objects.filter(parent_ob__in=policyId).values('file')
			try:
				for xx in file_name:
					file_obj = file_location+xx['file']
					object_data = PyPDF2.PdfFileReader(file_obj)
					NumPages = object_data.getNumPages()
					for i in range(0, NumPages):
						PageObj = object_data.getPage(i)
						Text = PageObj.extractText()
						ResSearch = re.search(String, Text)
						if ResSearch != None:
							file_rec = {"file_name" : xx['file']}
							# print("@@@@@@@@@@@", file_rec)
							file_Data.append(file_rec)
			except:
				pass
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
			file_name = ack_publicationname.objects.filter(parent_ob__in=policyId).values('file')
			try:
				for xx in file_name:
					file_obj = file_location+xx['file']
					object_data = PyPDF2.PdfFileReader(file_obj)
					NumPages = object_data.getNumPages()
					for i in range(0, NumPages):
						PageObj = object_data.getPage(i)
						Text = PageObj.extractText()
						ResSearch = re.search(String, Text)
						if ResSearch != None:
							file_rec = {"file_name" : xx['file']}
							# print("@@@@@@@@@@@", file_rec)
							file_Data.append(file_rec)
			except:
				pass
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
			file_name = InstructionUser.objects.filter(parent_ob__in=policyId).values('file')
			try:
				for xx in file_name:
					file_obj = file_location+xx['file']
					object_data = PyPDF2.PdfFileReader(file_obj)
					NumPages = object_data.getNumPages()
					for i in range(0, NumPages):
						PageObj = object_data.getPage(i)
						Text = PageObj.extractText()
						ResSearch = re.search(String, Text)
						if ResSearch != None:
							file_rec = {"file_name" : xx['file']}
							# print("@@@@@@@@@@@", file_rec)
							file_Data.append(file_rec)
			except:
				pass
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
			file_name = ack_guidelinesname.objects.filter(parent_ob__in=policyId).values('file')
			try:
				for xx in file_name:
					file_obj = file_location+xx['file']
					object_data = PyPDF2.PdfFileReader(file_obj)
					NumPages = object_data.getNumPages()
					for i in range(0, NumPages):
						PageObj = object_data.getPage(i)
						Text = PageObj.extractText()
						ResSearch = re.search(String, Text)
						if ResSearch != None:
							file_rec = {"file_name" : xx['file']}
							# print("@@@@@@@@@@@", file_rec)
							file_Data.append(file_rec)
			except:
				pass
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
			file_name = ack_Navyname.objects.filter(parent_ob__in=policyId).values('file')
			if request.GET.get('search')!= None:
				for xx in file_name:
					file_obj = file_location+xx['file']
					object_data = PyPDF2.PdfFileReader(file_obj)
					NumPages = object_data.getNumPages()
					for i in range(0, NumPages):
						PageObj = object_data.getPage(i)
						Text = PageObj.extractText()
						ResSearch = re.search(String, Text)
						if ResSearch != None:
							file_rec = {"file_name" : xx['file']}
							# print("@@@@@@@@@@@", file_rec)
							file_Data.append(file_rec)


			graph_records = {"name": x['submenu_name'], "y": graph_count}
			policyobjId.append(graph_records)

			bargraph_count = NavyUser.objects.filter(user__in=policyId).count()
			bragraph_records = {"name": x['submenu_name'], "y": bargraph_count}
			barobjIds.append(bragraph_records)
		# print(policyId,"sssssssssssss",file_Data)
		# file_location = os.getcwd()+"/media/"
		# for pdffile in file_Data:
		# 	file_obj = file_location+pdffile
		# 	object_data = PyPDF2.PdfFileReader(file_obj)
		# 	NumPages = object_data.getNumPages()
		# 	for i in range(0, NumPages):
		# 		PageObj = object_data.getPage(i)
		# 		Text = PageObj.extractText()
		# 		ResSearch = re.search(String, Text)
		# 		if ResSearch != None:
		# 			file_rec = {"file_name" : pdffile}
		# 			print(";;;;;;;;;;;;;;;;;;;;;;", file_rec)
	print("::::::::::::::::::::vvv", file_Data)
	data  = ({"asd":policyobjId,"barhraph": barobjIds,"knowledgetype" : request.GET.get('menubar'),"text_file": file_Data})

	return JsonResponse(data, safe=False)

class policyViewApi(APIView):
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



			policy_name =  Ack_submenu.objects.filter(id=id ).values()# | ack_submenu.objects.filter(parent_ob_id=id ).values()
			policy =[]

			policyId =  self.get_all_children(id,Ack_submenu)
			
			policy_name =  Ack_submenu.objects.filter(id__in=policyId )
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

def get_all_user_data(id,menubar,lists=None):
	policy_name =  menubar.objects.filter(id=id ).values()
	print("<<<<", policy_name)
	
class knowledgeMat(knowledgeGraphApi):

	def pagination_data(self,numpages, users,page):
		if numpages > 0:
			numpages =  numpages
			know_next = users.has_next()
			know_previous = users.has_previous()
			know_user_changes = users.has_other_pages()
			if know_next == True:
				know_next_page_number = users.next_page_number()
			if page >1:
				know_previous_page = users.previous_page_number()
				current_page = users.number
			else:
				 know_previous_page = 1
				 current_page = 1
			know_index = users.start_index()
			know_end = users.end_index()
			if know_next != True:
				know_record = {"numpages":numpages,"know_next":know_next, "know_previous":know_previous,"know_user_changes":know_user_changes, "know_previous_page":know_previous_page,"know_index":know_index,"know_end":know_end,"current_page":current_page}
			else:
				know_next_page_number = users.next_page_number()
				know_record = {"numpages":numpages,"know_next":know_next,"know_previous":know_previous,"know_user_changes":know_user_changes, "know_previous_page":know_previous_page,"know_index":know_index,"know_end":know_end,"current_page":current_page,"know_next_page_number":know_next_page_number}
			
            # else:

            	# know_record = {"class_numpage":know_numpages,"class_next":know_next,
             #        "class_previous":know_previous,"class_user_changes":know_user_changes,
             #        "class_previous_page":know_previous_page,"class_index":know_index,"class_end":know_end,"current_page":current_page,"class_next_page_number":know_next_page_number}
			# print(";;;;;;;;;;;;;;;;;;;;;;;;", know_record)
		else:
			know_record = {"numpages":numpages}
		return know_record

	def get(self, request):
		print("!!!!!!yyyyyyyyyyyyyyyyyyyyyyyyyy!!!!!!", request.GET )
		data_user= []
		if request.GET.get('menubar') == 'Policy':
			submenu = Ack_submenu.objects.filter(parent_ob_id=None,folder_type=2, status=2, file_type=request.GET.get('file_type'))
			if request.GET.get('page') == None:
				page =1
			else:
				page = int(request.GET.get('page'))
			paginator = Paginator(submenu,5)
			try:
				users = paginator.page(page)
			except PageNotAnInteger:
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			numpages = paginator.num_pages
			pagination_obj = self.pagination_data(numpages,users,page)

			serializer = serializers.AckenowledgeSubmenuSerializer(users,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=request.GET.get('mainId'))
			graph_data  = request.GET.get('menu_name')
			menu_name = Ack_submenu.objects.filter(submenu_name=graph_data).values('id')
			try:
				for graph_name in menu_name:
					# policyId =  get_all_user_data(graph_name['id'],Ack_submenu)
					policyy =  super(knowledgeMat, self).get_all_children(Ack_submenu, graph_name['id'])
					
					graph_rec = KnowledgeUser.objects.filter(user__in=policyy)
					
					paginator_user = Paginator(graph_rec,5)
				try:
					graph_users = paginator_user.page(page)
				except PageNotAnInteger:
					graph_users = paginator_user.page(1)
				except EmptyPage:
					graph_users = paginator_user.page(paginator.num_pages)
				numpages = paginator_user.num_pages
				data_user = serializers.policyUserSerializer(graph_users, many=True).data
				print("<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>", data_user)

			except:
				pass

			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
		if request.GET.get('menubar') == 'Publication':
			submenu = ack_subpublicationmenu.objects.filter(parent_ob_id=None,folder_type=2,  file_type=request.GET.get('file_type'))
			if request.GET.get('page') == None:
				page =1
			else:
				page = int(request.GET.get('page'))
			paginator = Paginator(submenu,5)
			try: 
				users = paginator.page(page)
			except PageNotAnInteger:
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			numpages = paginator.num_pages
			pagination_obj = self.pagination_data(numpages,users,page)

			serializer = serializers.AckenowledgepublicationSubmenuSerializer(users,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_publicationname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgePublicationMenuSerializer(policy_file, many=True)
		if request.GET.get('menubar') == 'Navy Orders':
			submenu = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None,folder_type=2,
			  file_type=request.GET.get('file_type'))
			if request.GET.get('page') == None:
				page = 1
			else:
				page = int(request.GET.get('page'))
			paginator = Paginator(submenu,5)
			try:
				users = paginator.page(page)
			except PageNotAnInteger:
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			numpages = paginator.num_pages
			pagination_obj = self.pagination_data(numpages,users,page)
			serializer = serializers.Ack_subNavy_OrderssmenuSerializer(users,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_Navyname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgeNavyOrdersSerializer(policy_file, many=True)
			
		if request.GET.get('menubar') == 'GuideLines':
			submenu = ack_subGuidelinesmenu.objects.filter(parent_ob_id=None,folder_type=2, 
			 file_type=request.GET.get('file_type'))
			if request.GET.get('page') == None:
				page = 1
			else:
				page = int(request.GET.get('page'))
			paginator = Paginator(submenu,5)
			try:
				users = paginator.page(page)
			except PageNotAnInteger:
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			numpages = paginator.num_pages
			pagination_obj = self.pagination_data(numpages,users,page)
			serializer = serializers.AckenowledgeGuidelinesSubmenuSerializer(users,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_guidelinesname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckguideLineSerializer(policy_file, many=True)
			# data_record['obj'] = data_obj.data
			
		elif request.GET.get('menubar') == 'Navy Instruction' :
			# print("£££££££££££ssss",id)
			submenu = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None,folder_type=2, 
			 file_type=request.GET.get('file_type'))
			if request.GET.get('page') == None:
				page = 1
			else:
				page = int(request.GET.get('page'))
			paginator = Paginator(submenu,5)
			try:
				users = paginator.page(page)
			except PageNotAnInteger:
				users = paginator.page(1)
			except EmptyPage:
				users = paginator.page(paginator.num_pages)
			numpages = paginator.num_pages
			pagination_obj = self.pagination_data(numpages,users,page)
			serializer = serializers.AckNavyInstmenuSerializer(users,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_NavyInstructionname.objects.filter(parent_ob_id=request.GET.get('mainId'))
			data_obj = serializers.AckenowledgeNavyInstructionSerializer(policy_file, many=True)
		data_record['obj'] = data_obj.data
		data_record['users'] = data_user
		data_record['pagination'] = pagination_obj

		return Response(data_record)
import PyPDF2
import re

class AckpolicyAPI(APIView):
	def get(self,request, id):

		if request.GET.get('menubar') == 'Policy':
			submenu = Ack_submenu.objects.filter(parent_ob_id=id,folder_type=2, status=2, file_type=request.GET.get('file_type'))

			serializer = serializers.AckenowledgeSubmenuSerializer(submenu,many=True)
			data_record = {"policy": serializer.data}
			policy_file = ack_subMenuPolicyFile.objects.filter(parent_ob_id=id)
			data_obj = serializers.ack_subMenuPolicyFileSubmenuSerializer(policy_file, many=True)
			
			data_record['obj']  = data_obj.data

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
        print("sudha",os.getcwd())
        menu_id = graphDetail.objects.get(menu_detail=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id).id
        try:
        	graphDetailUsed.objects.create(menu_detail_id=menu_id, menu_user=User.objects.get(username=request.user.username))
        except:
        	pass
        if request.GET.get('menutype') =='Policy' :
            policy_data = Ack_submenu.objects.filter(parent_ob_id=None, status=2, file_type=1,
             parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            # policy_ob = Ack_submenu.objects.filter(parent_ob_id=None, status=2, file_type=1,
            #  parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id).select_related('parent_ob').all()
            # print(":::::::::::::::::::::::", policy_ob.query)
            policy_obj = Ack_submenu.objects.filter(parent_ob_id=None)
            policy_id = self.get_all_child(Ack_submenu,request.GET.get('menutype'),ack_subMenuPolicyFile)
            
        elif request.GET.get('menutype') =='Publication' :
            policy_data = ack_subpublicationmenu.objects.filter(parent_ob_id=None, file_type=1, 
            	parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subpublicationmenu.objects.all().order_by("-id")
            policy_id = self.get_all_child(ack_subpublicationmenu,request.GET.get('menutype'),ack_publicationname)

        elif request.GET.get('menutype') =='GuideLines' :
            policy_data = ack_subGuidelinesmenu.objects.filter(parent_ob_id=None, file_type=1, 
            	parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subGuidelinesmenu.objects.all().order_by("-id")
            policy_id = self.get_all_child(ack_subGuidelinesmenu,request.GET.get('menutype'),ack_guidelinesname)

        elif request.GET.get('menutype') =='Standards' :
            policy_data = ack_subStandardsmenu.objects.filter(parent_ob_id=None,  
            	file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subStandardsmenu.objects.all().order_by("-id")
            policy_id = self.get_all_child(ack_subStandardsmenu,request.GET.get('menutype'),ack_Standardsname)

        elif request.GET.get('menutype') == 'Navy Instruction' :
            policy_data = ack_subNavy_Instructionssmenu.objects.filter(parent_ob_id=None, 
            	file_type=1, parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subNavy_Instructionssmenu.objects.all().order_by("-id")
            policy_id = self.get_all_child(ack_subNavy_Instructionssmenu,request.GET.get('menutype'),ack_Standardsname)
   

        elif request.GET.get('menutype') =='Navy Orders' :
            policy_data = ack_subNavy_Orderssmenu.objects.filter(parent_ob_id=None, file_type=1, 
            	parent_id=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id)
            policy_obj = ack_subNavy_Orderssmenu.objects.all().order_by("-id")
            policy_id = self.get_all_child(ack_subNavy_Orderssmenu,request.GET.get('menutype'),ack_Navyname)

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

from rest_framework import generics
from rest_framework import filters
class ProductList(generics.ListAPIView):
	queryset = Ack_submenu.objects.all()
	serializer_class = serializers.AckenowledgeSubmenuSerializer
	search_fields = ['ack_submenu_children__submenu_name']
	# filter_backends = (DjangoFilterBackend,)
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	filterset_fields = ['ack_submenu_children__submenu_name']

class PublicList(generics.ListAPIView):
	queryset = ack_subpublicationmenu.objects.all()
	serializer_class = serializers.AckenowledgepublicationSubmenuSerializer
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	search_fields = ['ack_publication_children__submenu_name']
	filterset_fields = ['ack_publication_children__submenu_name']

class guideList(generics.ListAPIView):
	queryset = ack_subGuidelinesmenu.objects.all()
	serializer_class = serializers.AckenowledgeGuidelinesSubmenuSerializer
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	search_fields = ['guidelinesMenues__submenu_name']
	filterset_fields = ['guidelinesMenues__submenu_name']


class instrctionList(generics.ListAPIView):
	queryset = ack_subNavy_Instructionssmenu.objects.all()
	serializer_class = serializers.AckNavyInstmenuSerializer
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	search_fields = ['navyinstruction_name__submenu_name']
	filterset_fields = ['navyinstruction_name__submenu_name']


class navyordersList(generics.ListAPIView):
	queryset = ack_subNavy_Orderssmenu.objects.all()
	serializer_class = serializers.Ack_subNavy_OrderssmenuSerializer
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	search_fields = ['navyOrders_name__submenu_name']
	filterset_fields = ['navyOrders_name__submenu_name']



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
			manu_cnt = Ack_submenu.objects.filter(parent_id=menu['id']).count()
			menu_count.append(manu_cnt)

		context_data['data'] = menu_obj
		context_data['labels'] = menu_count



		return render(request, self.template_name, context_data)
