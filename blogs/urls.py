from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogs import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
#router.register(r'blog_viewss', views.AccountViewSet)

urlpatterns = [
    re_path(r'^blog_list/$', views.blogViews.as_view(), name="blog_list"),
    re_path(r'^addblog/$', views.addblogViews.as_view(), name="addblog"),
    re_path(r'^addcommment/(?P<id>[0-9]+)/$', views.editBlogComemnt.as_view(), name="addcommment"),
    re_path(r'^blog_view/$', views.BlogAPIView.as_view(), name="blog_view"),
    re_path('', include(router.urls)),

    ]