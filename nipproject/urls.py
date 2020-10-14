"""nipproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from acknowledge import views as ack_views
from application import views as app_views
from user import views as user_views

from blogs import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
#other_sites
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^home/$', app_views.headingViews.as_view(), name="home"),
    url(r'^mainhome/$', app_views.mainheadingViews.as_view(), name="mainhome"),
    url(r'^information/$', app_views.mainheadingssViews.as_view(), name="information"),
    url(r'^homes/$', app_views.mainheadingViews.as_view(), name="homes"),
    url(r'^homeicon/$', app_views.verticalMenuViews.as_view(), name="homeicon"),
    url(r'^homesmain/$', app_views.verticalMenubarViews.as_view(), name="homesmain"),
    url(r'^homes/temp/$', app_views.verticaltabViews.as_view(), name="temp"),

    url(r'^menu_detail/$', app_views.MenuApiView.as_view(), name="menu_detail"),

    url(r'^other_sites/$', app_views.OtherSitesViews.as_view(), name="other_sites"),

    url(r'^applicationobj_list/(?P<drink_name>\D+)/(?P<string_name>\D+)/$', app_views.applicationobViews.as_view(), name="applicationobj_list"),
    ##########################subDirectory############################################################################################
    url(r'^subdirectory/(?P<drink_name>\D+)/(?P<string_name>\D+)/$', app_views.subdirectoryViews.as_view(), name="subdirectory"),
    url(r'^commander/$', app_views.WingCommanderAPI.as_view(), name="commander"),
    url(r'^policy/$', app_views.MypolicyAPI.as_view(), name="policy"),
    url(r'^publication/$', app_views.MypublicationAPI.as_view(), name="publication"),
    url(r'^news_detail/$', app_views.MyNewsAPI.as_view(), name="news_detail"),
    url(r'^login/$', app_views.LoginViews.as_view(), name='login'),
    url(r'^article/$', app_views.index, name='article'),
    url(r'^application_list/(?P<id>[0-9]+)/$', app_views.ApplicationViewApi.as_view(), name="application_list"),



    ##########################################Acknowledge Urls###########################

    url(r'^mainnav/$', ack_views.ParentViewApi.as_view(), name="mainnav"),
    url(r'^ack_detail/$', ack_views.AcknowledgeAPI.as_view(), name="ack_detail"),
	url(r'^ackpolicy/$', ack_views.acknowledgeViews.as_view(), name="ackpolicy"),
    url(r'^graphview/$', ack_views.graphCount, name="graphview"),
    url(r'^filterview/$', ack_views.ProductList.as_view(), name="filterview"),
    url(r'^PublicfilterList/$', ack_views.PublicList.as_view(), name="PublicfilterList"),
    url(r'^guidefilterList/$', ack_views.guideList.as_view(), name="guidefilterList"),
    url(r'^instructionfilterList/$', ack_views.instrctionList.as_view(), name="instructionfilterList"),
    url(r'^navyorderfilterList/$', ack_views.navyordersList.as_view(), name="navyorderfilterList"),
    # url(r'^usergraphview/$', ack_views.policygraph, name="usergraphview"),
	#url(r'^ackpublication/$', ack_views.acknowledgepublicationViews.as_view(), name="ackpublication"),

	url(r'^publication_view/(?P<id>[0-9]+)/$', ack_views.policyViewApi.as_view(), name="publication_view"),
	url(r'^publication_newview/(?P<id>[0-9]+)/(?P<sm_id>[0-9]+)/$', ack_views.policynewViewApi.as_view(), name="publication_newview"),
	url(r'^publication_newviewobj/(?P<id>[0-9]+)/(?P<sm_id>[0-9]+)/$', ack_views.policyViewobjApi.as_view(), name="publication_newviewobj"),

	url(r'^knowledge/$', ack_views.ack_menudetail.as_view(), name="knowledge"),
    #url(r'^knowledgemenu/$', ack_views.knowmenuobjApi.as_view(), name="knowledgemenu"),
    url(r'^knowpubmenu/$', ack_views.publicationfileApi.as_view(), name="knowpubmenu"),



	url(r'^ack_publicationdetail/$', ack_views.AxknowledgePublicAPI.as_view(), name="ack_publicationdetail"),
	url(r'^policyView/(?P<id>[0-9]+)/$', ack_views.AckpolicyAPI.as_view(), name="policyView"),
    url(r'^policyViewmat/$', ack_views.knowledgeMat.as_view(), name="policyViewmat"),
    



    ###############################blog####################

    url(r'^blog_list/$', blog_views.blogViews.as_view(), name="blog_list"),
    url(r'^addblog/$', blog_views.addblogViews.as_view(), name="addblog"),
    url(r'^addcommment/(?P<id>[0-9]+)/$', blog_views.editBlogComemnt.as_view(), name="addcommment"),
    url(r'^blog_view/$', blog_views.BlogAPIView.as_view(), name="blog_view"),

    ##########################User########################
    url(r'^user_ob/$', user_views.userViewset.as_view({'get': 'list', 'post': 'create'}), name="user_ob"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
