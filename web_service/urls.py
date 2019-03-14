from django.conf.urls import url
from web_service import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^webservice/$', views.snippet_list),
    #url(r'^webservice/(?P<pk>[0-9]+)/$', views.snippet_detail)
    url(r'^web_s/(?P<pk>[0-9]+)/$',views.snippet_list)

]

