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
     NavyUser, GuideLinesUser, StandardUser)
from django.contrib.auth import get_user_model
from acknowledge import serializers
from users import serializers
from acknowledge.views import get_all_children

from django_filters.rest_framework import DjangoFilterBackend
pagination_ob = settings.PAGINATION_SIZE
import os

from django.shortcuts import render, redirect



class policyview(TemplateView):
	template_name = "backend/index.html"
	def get(self, request, id=None):
		context_data = {}
		error = ''
		context_data['error'] = error
		submenus = Ack_submenu.objects.filter(parent_ob_id=None, folder_type='2')
		# policy_name =  Ack_submenu.objects.filter(parent_ob_id=None).values('submenu_name','id')
		# for x in policy_name:
		# 	policyId  =  get_all_children(x['id'], Ack_submenu )
		# 	print("::::::::::::::::::", policyId)
		context_data['menu'] = submenus
		return render(request, self.template_name, context_data)



class userList(APIView):
	def get(self, request, id=None):
		print(request.GET.get('id'))
		user_data = User.objects.all()
		serializer =  serializers.userSerializer(user_data, many=True)
		return Response(serializer.data)





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
		return render(request, self.template_name, context_data)


class acknowledgedataViews(TemplateView):
    template_name = "backend/permissionfile.html"

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
        
        # menu_id = graphDetail.objects.get(menu_detail=acknoledge_menu.objects.get(menu_name=request.GET.get('menutype')).id).id
        # try:
        # 	graphDetailUsed.objects.create(menu_detail_id=menu_id, menu_user=User.objects.get(username=request.user.username))
        # except:
        # 	pass
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





