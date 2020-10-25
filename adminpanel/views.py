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
from acknowledge.models import (ack_subStandardsmenu, ack_Navyname, ack_subNavy_Orderssmenu,
 ack_subGuidelinesmenu, ack_Standardsname,  graphDetail,ack_guidelinesname,
  ack_subMenuPolicyFile, ack_subNavy_Instructionssmenu,graphDetailUsed,
   ack_subpublicationmenu, ack_publicationname, acknoledge_menu,parent_menu,
   Ack_submenu, ack_policyname, ack_policypolicyfile,
    ack_NavyInstructionname, KnowledgeUser, PublicationUser, InstructionUser,
     NavyUser, GuideLinesUser, StandardUser, UploadPdf)
from django.contrib.auth import get_user_model
from acknowledge import serializers

from django_filters.rest_framework import DjangoFilterBackend
pagination_ob = settings.PAGINATION_SIZE
import os

from django.shortcuts import render, redirect



class adminview(TemplateView):
	template_name = "backend/addpolicy.html"
	def get(self, request, id=None):
		context_data = {}
		error = ''
		submenus = Ack_submenu.objects.filter(folder_type='2')
		
		context_data['menu'] = submenus 
		context_data['error'] = error
		return render(request, self.template_name, context_data)

	def post(self, request):
		# print("::::::::::::::", request.POST.get('addpolicy'))
		context_data = {}
		error = ''
		submenus = Ack_submenu.objects.filter(folder_type='2')
		if request.POST.get('addpolicy') == 'Add Policy':
			fileFolder = request.POST.get('filfolder')
			submenu_name = request.POST.get('policy_name')
			if request.POST.get('parentpolicy') == ' ':
				parent_policy = None
			else:
				parent_policy = request.POST.get('parentpolicy')			
			policytype = request.POST.get('policytype')
			if request.POST.get('filfolder') == '2':
				menu_post = Ack_submenu.objects.create(submenu_name=submenu_name, folder_type=fileFolder, 
					file_type=policytype, parent_ob_id=parent_policy, parent_id=1 )
			else:
				policyfile = request.FILES.getlist('policyfile')
				if policyfile == []:
					error = "Please Upload the Pdf file"


				for pfile in policyfile:
					name,extesion = os.path.splitext(str(pfile))
					
					if name == '':
						error ="Please Upload the file"
					if parent_policy  == None:
						error = "Please Select the parent Policy Type"

					submenu_name = name
					if error  == '':
						menu_post = Ack_submenu.objects.create(submenu_name=submenu_name, folder_type=fileFolder, 
						file_type=policytype, parent_ob_id=parent_policy, parent_id=1, file=pfile )
					



		context_data['menu'] = submenus 
		context_data['error'] = error
		print("::::::::::::::::::", error)




		return render(request, self.template_name, context_data)





