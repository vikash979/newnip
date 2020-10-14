from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogs.models import blog_model,Comment
from django.views.generic import TemplateView , View
from django.conf import settings
from . import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from users.models import User
# from . import serializers
from django.template.loader import get_template

from django.views.generic import View
import json
from django.http import JsonResponse
from application.views import PaginationHandlerMixin, BasicPagination

def paginator_maker(request_args,model):
    page = request_args.GET.get("page")



class blogViews(TemplateView):
	template_name = "blog/blogs.html"
	def get(self, request, id=None):
		context_data = {}
		blog_name = blog_model.objects.all().values().order_by("-id")
		pagination_ob= 4
		paginator = Paginator(blog_name,pagination_ob)

		if request.GET.get('page')==None:
			page =1
		else:
			page = int(request.GET.get('page'))
		try:
			users = paginator.page(page)
		except PageNotAnInteger :
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)


		blog_comment = []
		for blog_rec in blog_name:
			blog_obj = {"blog_heading":blog_rec['blog_heading'],"bloc_id":blog_rec['id'],"blog_count":blog_rec['blog_count']}

			comment_obj = Comment.objects.filter(object_id=blog_rec['id']).values('text','user','added_on','id').order_by("-id")[:1]
			comment_ob =[]



			for comment_data in comment_obj :

				comment_rec = {"comment_data":comment_data['text'],"added_date":comment_data['added_on'],"comment_id":comment_data['id']}
				user_data= User.objects.filter(id=comment_data['user']).values('email')
				user_record = []

				for user_ob in user_data:

					comment_rec["user_name"] = user_ob['email']

				comment_ob.append(comment_rec)
				blog_obj['comments']= comment_ob
			blog_comment.append(blog_obj)



		context_data['staff_image'] = users
		program_numpages = paginator.num_pages
		program_numpages = program_numpages+1
		context_data['PAGINATION_COUNT'] = range(1,program_numpages)

        #prnt("@@@@@@@@",context_data)
		return render(request, self.template_name, context_data)

class addblogViews(TemplateView):
	template_name = "blog/addblog.html"
	def post(self, request, id=None):
		context_data = {}
		blog = request.POST.get('blog')
		blog_comment = request.POST.get('comment')
		user_name = request.POST.get('user_name')
		blog = blog.strip()
		if len(blog)>0:
			blog_ob = blog_model.objects.create(blog_heading=blog,created_by=User.objects.get(id=user_name))
			blog_comment = Comment.objects.create(text=blog_comment,content_object=blog_ob,user=User.objects.get(id=user_name) )
		return render(request, self.template_name, context_data)


class editBlogComemnt(TemplateView):
	template_name = "blog/addcommment.html"
	def get(self, request, id=None):

		context_data = {}
		blog_name = blog_model.objects.filter(id=id).values().order_by("-id")
		blog_comment = []
		for blog_rec in blog_name:
			blog_obj = {"blog_heading":blog_rec['blog_heading'],"bloc_id":blog_rec['id'],"blog_count":blog_rec['blog_count']}

			comment_obj = Comment.objects.filter(object_id=blog_rec['id']).values('text','user','added_on','id').order_by("-id")
			comment_ob =[]
			for comment_data in comment_obj :
				comment_rec = {"comment_data":comment_data['text'],"added_date":comment_data['added_on'],"comment_id":comment_data['id']}
				user_data= User.objects.filter(id=comment_data['user']).values('email')
				user_record = []

				for user_ob in user_data:
					#print(user_ob['email'])
					#user_name = {"email": user_ob['email']}
					comment_rec["user_name"] = user_ob['email']

				comment_ob.append(comment_rec)
				blog_obj['comments']= comment_ob
			blog_comment.append(blog_obj)



		context_data['staff_image'] = blog_comment
		context_data['user_id'] = id

		return render(request, self.template_name, context_data)

	def post(self, request, id=None):
		context_data = {}


		#blog = request.POST.get('blog')
		blog_comments = request.POST.get('comment')
		user_name = request.POST.get('user_name')
		#blog = blog.strip()
		if len(blog_comments)>0:
			#blog_ob = blog_model.objects.create(blog_heading=blog,created_by=CustomUser.objects.get(id=user_name))
			blog_commnt = Comment.objects.create(text=blog_comments,content_object=blog_model.objects.get(id=id),user=User.objects.get(id=user_name) )

		blog_name = blog_model.objects.filter(id=id).values().order_by("-id")
		blog_comment = []
		for blog_rec in blog_name:
			blog_obj = {"blog_heading":blog_rec['blog_heading'],"bloc_id":blog_rec['id'],"blog_count":blog_rec['blog_count']}

			comment_obj = Comment.objects.filter(object_id=blog_rec['id']).values('text','user','added_on','id').order_by("-id")
			comment_ob =[]
			for comment_data in comment_obj :
				comment_rec = {"comment_data":comment_data['text'],"added_date":comment_data['added_on'],"comment_id":comment_data['id']}
				user_data= User.objects.filter(id=comment_data['user']).values('email')
				user_record = []

				for user_ob in user_data:
					#print(user_ob['email'])
					#user_name = {"email": user_ob['email']}
					comment_rec["user_name"] = user_ob['email']

				comment_ob.append(comment_rec)
				blog_obj['comments']= comment_ob
				blog_comments = ''
			blog_comment.append(blog_obj)
		context_data['staff_image'] = blog_comment
		context_data['user_id'] = id
		return render(request, self.template_name, context_data)



class BlogAPIView(APIView):
    #pagination_class = BasicPagination
    serializer_class = serializers.BlogSerializer

    def get(self, request, format=None, *args, **kwargs):
    	print("@@@@@@@@@@@@@@",request.GET.get("parent_id"))
    	instance = blog_model.objects.filter(id=request.GET.get("parent_id")).values()
    	serializer = serializers.BlogSerializer(instance,many=True)
    	return Response(serializer.data)


        # if page is not None:
        #     serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        # else:
        #     serializer = self.serializer_class(instance, many=True)



    def post(self, request, *args, **kwargs):

    	blogcount = 1;
    	blogcount +=int(request.data.get('viewcount'))
    	instance  = blog_model.objects.filter(id=request.data.get("parent_id")).update(blog_count=blogcount)
    	instances = Comment.objects.filter(object_id=request.data.get("parent_id"))
    	instance  = blog_model.objects.filter(id=request.data.get("parent_id"))
    	serializer = serializers.BlogSerializer(instance,many=True)
    	return Response(serializer.data[:1])


class AccountViewSet(viewsets.ModelViewSet):
	queryset = blog_model.objects.all()
	serializer_class = serializers.BlogSerializer

	def create(self,request):
		print("helllooo")
		return Response({"data":"sd"})
