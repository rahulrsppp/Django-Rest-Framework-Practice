from django.conf.urls import url
from web_service.api_1.views import MyRudOperations,MyPostApiOperations
from web_service import views

urlpatterns = [
    #url(r'^(?P<pk>\d+)/$',MyRudOperations.as_view(),name='post-rud'),
    url(r'^list/$',MyRudOperations.as_view(),name='listData'),
    url(r'^$',MyPostApiOperations.as_view(),name='post_api')
]
