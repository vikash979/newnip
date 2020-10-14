from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from application import views
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
#router.register(r'dit', views.parentViewViewset)
#router.register(r'users', views.UserViewSet)


urlpatterns = [

    re_path(r'^applicationheasing/$', views.headingViews.as_view(), name="applicationheasing"),
    re_path(r'^menu_detail/$', views.MenuApiView.as_view(), name="menu_detail"),
    re_path(r'^applicationobj_list/(?P<drink_name>\D+)/(?P<string_name>\D+)/$', views.applicationobViews.as_view(), name="applicationobj_list"),
    ##########################subDirectory############################################################################################
    re_path(r'^subdirectory/(?P<drink_name>\D+)/(?P<string_name>\D+)/$', views.subdirectoryViews.as_view(), name="subdirectory"),
    re_path(r'^commander/$', views.WingCommanderAPI.as_view(), name="commander"),
    re_path(r'^policy/$', views.MypolicyAPI.as_view(), name="policy"),
    re_path(r'^publication/$', views.MypublicationAPI.as_view(), name="publication"),
    re_path(r'^news_detail/$', views.MyNewsAPI.as_view(), name="news_detail"),
    re_path(r'^login/$', views.LoginViews.as_view(), name='login'),
    re_path(r'^article/$', views.index, name='article'),
    #re_path(r'^logins/$', views.login_user, name='logins'),

    re_path(r'^application_list/(?P<id>[0-9]+)/$', views.ApplicationViewApi.as_view(), name="application_list"),
]
