from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from application.models import application_menu, application_submenu,application_parent_menu, news, wing_commander, staff_image,publication, policy, Article
from django.views.generic import TemplateView , View
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from . import serializers
from django.template.loader import get_template
from django.contrib.auth import authenticate,login,logout



def login_api_required(login_url=None):
    def function(func):
        def wrapper(request):
            if  not request.user.is_authenticated:
                return HttpResponseRedirect("/application/login/")

            return func(request)
        return wrapper
    return function


def login_required_custom(login_url=None):
    def function(func):
        def wrapper(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/login/")
            return func(self, request, *args, **kwargs)
        return wrapper
    return function

class headingViews(TemplateView):
	template_name = "verticalmenu/index2.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):
		context_data = {}
		context_data['error'] = ''
		context_data['staff_image']  = wing_commander.objects.all().order_by("id")[:8]
		#context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)


################end index.htmljs

class mainheadingViews(TemplateView):
	template_name = "application/index6.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):


		#hostname = socket.gethostname()
		#IPAddr = socket.gethostbyname(hostname)
		#print(IPAddr)

		context_data = {}
		context_data['error'] = ''
		context_data['staff_image'] = staff_image.objects.all().order_by("-id")[4:8]
		context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)



class mainheadingssViews(TemplateView):
	template_name = "application/index3.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):


		#hostname = socket.gethostname()
		#IPAddr = socket.gethostbyname(hostname)
		#print(IPAddr)

		context_data = {}
		context_data['error'] = ''
		context_data['staff_image'] = staff_image.objects.all().order_by("-id")[4:8]
		context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)

class verticaltabViews(TemplateView):
	template_name = "application/temp.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):
		context_data = {}
		context_data['error'] = ''
		context_data['staff_image'] = staff_image.objects.all().order_by("-id")[4:8]
		context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)


class verticalMenuViews(TemplateView):
	template_name = "application/index8.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):
		context_data = {}
		context_data['error'] = ''
		context_data['staff_image'] = staff_image.objects.all().order_by("-id")[4:8]
		context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)


class OtherSitesViews(TemplateView):
    template_name = "application/NavyOtherSites.html"

    def get(self, request):
        context_data = {}


        return render(request, self.template_name, context_data)

class verticalMenubarViews(TemplateView):
	template_name = "verticalmenu/index.html"
	#@login_required_custom(login_url='/')
	def get(self, request, id=None):
		context_data = {}
		context_data['error'] = ''
		context_data['staff_image'] = staff_image.objects.all().order_by("-id")[4:8]
		context_data['image'] = staff_image.objects.all().order_by("-id")[:4]

		return render(request, self.template_name, context_data)



class MenuApiView(APIView):
	def get_queryset(self):
		return application_menu.objects.all()

	def get(self, request,*args, **kwargs):

		try:


			queryset = application_parent_menu.objects.all()

			#queryset = application_parent_menu.objects.filter(menu_type=1)


			serializer = serializers.ParentMenuerializer(queryset,many=True)
			data = serializer.data
		except:
			data = {}

		return Response(data)



class applicationobViews(TemplateView):
	template_name = "application/folder.html"
	def get(self, request, drink_name,string_name):

		context_data = {}

		if request.GET.get('folder_id')=='' or request.GET.get('folder_id')==None:
			menuobj_id = application_menu.objects.filter(menu_name=string_name).values('id')[0]['id']
			# hh = application_submenu.objects.filter(menu_id_id=menuobj_id).values('id')[0]['id']
			# hhh = application_submenu.objects.filter(submenu_name=string_name).values('id')[0]['id']


			#menu_ob = application_submenu.objects.filter(menu_id_id=request.GET.get('folder_id')).values()
			#return HttpResponse("dsdsds")
			return HttpResponseRedirect("/application/subdirectory/"+drink_name+"/"+string_name+"/?folder_id="+str(menuobj_id))



class subdirectoryViews(TemplateView):
	template_name = "application/folder.html"
	def obj_data(self,idd):
		hhhh = application_menu.objects.filter(parent_ob=idd).values()
		for xxx in hhhh:
			print("@@@@@@@@@@@",xxx)

	def ob_data(self,ids,list_objj):


		#list_obj=[list_objj]

		#print("!!!!!!!!!!!",list_obj)

		mmm = application_menu.objects.filter(parent_ob_id=ids).values('menu_name','id','parent_ob')
		nn =[]

		for xx in mmm:
			print(xx['id'])

			#list_objj['subs']=xx
			#klkk= (self.ob_data(xx['id'],list_objj))

		#print(nn)
		#print("##",list_obj)



			#list_obj.append(tt)
			# =  self.ob_data(xx['id'],list_obj=[])


	def megafolder(self,megaid,tt, listdetail=[]):
		listdetail.append(tt)
		mmmnn = application_menu.objects.filter(parent_ob_id=megaid).values('menu_name','id','folder_type')
		for mmmmmm in mmmnn:
			if mmmmmm['folder_type']==2:
				seccc = mmmmmm
				tt['menu_name'] =seccc
				#print(":::",secc)
				self.megafolder(seccc['id'],seccc)
		print("rrrr",tt)

	def get(self, request, drink_name,string_name):
		context_data = {}

		mm = application_menu.objects.filter(parent_ob_id=request.GET.get('folder_id')).values('menu_name','id','parent_ob','folder_type','file','added_on')


		zz = application_menu.objects.filter(menu_name=string_name,folder_type=2).values('menu_name','id','folder_type')
		#print("@@##1",zz)
		ss = []
		seconding = []
		thirds = []
		forths = []
		first_folder = ''
		for kk in zz:
			tt = kk
			if tt['folder_type']==2:
				first_folder = tt
				#print("#$%",tt)
				#aaaa = self.megafolder(tt['id'],tt)

				mmm = application_menu.objects.filter(parent_ob_id=tt['id']).values('menu_name','id','folder_type')


				for mmmm in mmm:
					if mmmm['folder_type']==2:
						secc = mmmm


						seconding.append(mmmm)
						first_folder["menu_item"]= seconding

						#print("@@@@@@@@",seconding)
						thirds =[]
						mmmmmm = application_menu.objects.filter(parent_ob_id=mmmm['id']).values('menu_name','id','folder_type','parent_ob')
						for yyy in mmmmmm:
						 	if yyy['folder_type']==2:
						 		#print("fdfffffff",yyy)
						 		thir =yyy
						 		thirds.append(yyy)
								#print("@#$$$$$$$$$$$$",thirds)
						 		secc["menu_items"] =thirds
						 		zzz = application_menu.objects.filter(parent_ob_id=yyy['id']).values('menu_name','id','folder_type','parent_ob')
						 		forths = []
						 		for zzzz in zzz:
						 			if zzzz['folder_type']==2:
						 				forths.append(zzzz)
						 				thir["menu_items"]=forths

		ss.append(first_folder)
		#print("####################",ss)

		mmmn = []
		list_obj = {}


		context_data['parent_menu'] = drink_name
		context_data['menu_detail'] = string_name
		context_data['folder_obj'] = mm
		#print("############@@",request.GET.get('folder_id'),mm)
		context_data['folder_objs'] = ss
		context_data['folder_id'] = request.GET.get('folder_id')
		#context_data['folder_obj'] = application_submenu.objects.filter(id=request.GET.get('folder_id')).values()

		return render(request, self.template_name,context_data)



class ApplicationViewApi(APIView):
	def get_object(self):
		try:
			return application_menu.objects.all()
		except application_menu.DoesNotExist:
			return Http404

	def get(self,request, id,format=None):
		context_data = {}
		mega_obj = application_menu.objects.filter(parent_ob_id=id).values().order_by("-id")
		serializer = serializers.ApplicationmenuSerializer(mega_obj,many=True)

		return Response(serializer.data)



class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

from rest_framework.pagination import PageNumberPagination

class BasicPagination(PageNumberPagination):
    #page_size_query_param = 'limit'
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class MyListAPI(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = serializers.ApplicationMenuobjSerializer

    def get(self, request, format=None, *args, **kwargs):
        instance = application_menu.objects.filter(menu_name=request.GET.get('parent_id'),folder_type=2).values('menu_name','id','folder_type')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
        	serializer = self.serializer_class(instance, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class MypolicyAPI(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = serializers.PolicyobjSerializer
	def get(self, request, format=None, *args, **kwargs):
		instance = policy.objects.all()

		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)

		else:
			serializer = self.serializer_class(instance, many=True)
		return Response(serializer.data)


class MypublicationAPI(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = serializers.PublicationSerializer

    def get(self, request, format=None, *args, **kwargs):
        instance = publication.objects.all()
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
        	serializer = self.serializer_class(instance, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class WingCommanderAPI(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = serializers.wing_commanderSerializer

    def get(self, request, format=None, *args, **kwargs):
        instance = wing_commander.objects.all().order_by("id")[:8]
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
        	serializer = self.serializer_class(instance, many=True)

        return Response(serializer.data)



#########################Publication/////////////

class MypublicationAPI(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = serializers.PublicationSerializer

	def get(self, request, format=None, *args, **kwargs):
		instance = publication.objects.all()
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
		else:
			serializer = self.serializer_class(instance, many=True)
		return Response(serializer.data)




###################################news detail
class MyNewsAPI(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = serializers.NewsMenuuobjSerializer


	def get(self, request, format=None, *args, **kwargs):
		instance = news.objects.all().order_by("-id")[:4]
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
		else:
			serializer = self.serializer_class(instance, many=True)
		return Response(serializer.data)


class LoginViews(TemplateView):
	template_name = "application/login.html"
	def get(self,request):
		context_data = {}
		if request.user.is_authenticated:
			return HttpResponseRedirect("/home/")
		else:
			return render(request, self.template_name, context_data)

	def post(self,request):
		context_data ={}
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				request.session['fav_color'] = 'blue'

				return HttpResponseRedirect("/home/")
			else:
				context_data['error'] = {"errors" : "Username or Password is not correct"}
				return render(request, self.template_name, context_data)
			return render(request, self.template_name, context_data)




def index(request):
	article = Article.objects.all()
	context  = {"article":article}

	return render(request,"index.html",context)
