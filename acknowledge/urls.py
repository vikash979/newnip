from django.urls import re_path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from acknowledge import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
router = DefaultRouter()
#router.register(r'dit', views.parentViewViewset)
#router.register(r'users', views.UserViewSet)


urlpatterns = [

	re_path(r'^ack_detail/$', views.AcknowledgeAPI.as_view(), name="ack_detail"),
	re_path(r'^ackpolicy/$', views.acknowledgeViews.as_view(), name="ackpolicy"),
	re_path(r'^ackpublication/$', views.acknowledgepublicationViews.as_view(), name="ackpublication"),

	re_path(r'^publication_view/(?P<id>[0-9]+)/$', views.policyViewApi.as_view(), name="publication_view"),
	re_path(r'^publication_newview/(?P<id>[0-9]+)/(?P<sm_id>[0-9]+)/$', views.policynewViewApi.as_view(), name="publication_newview"),
	re_path(r'^publication_newviewobj/(?P<id>[0-9]+)/(?P<sm_id>[0-9]+)/$', views.policyViewobjApi.as_view(), name="publication_newviewobj"),

	re_path(r'^ackpolicy_detail/$', views.ack_menudetail.as_view(), name="ackpolicy_detail"),
	#re_path(r'^pie-chart/$', views.pie_chart, name="pie-chart"),
	#re_path(r'^sendjson/$', views.send_json, name="sendjson"),
	re_path(r'^ack_publicationdetail/$', views.AxknowledgePublicAPI.as_view(), name="ack_publicationdetail"),
	re_path(r'^policyView/(?P<id>[0-9]+)/$', views.AckpolicyAPI.as_view(), name="policyView"),
	#path('pie-chart/', views.pie_chart, name='pie-chart'),
	###################userupdate############################


]
urlpatterns = format_suffix_patterns(urlpatterns)
