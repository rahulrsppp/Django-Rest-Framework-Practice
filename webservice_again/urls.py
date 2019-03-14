from django.contrib.auth.views import LoginView
from django.urls import include

from webservice_again.viewset import LoginViewSet, RegistrationViewset, CheckUserExistence, LogoutViewSet, \
    GetVoterByUserType
from .router import myRouters
from django.conf.urls import url
from rest_framework.authtoken import views
from django.contrib.auth import login
from webservice_again.viewset import UpdateVoter


urlpatterns = [

    url('api/', include(myRouters.urls)),
    url('password-auth/', views.obtain_auth_token, name= "password-auth"),
     url('checkUserExistence', CheckUserExistence.as_view(), name= "checkUserExistence"),

     url('api/login', LoginViewSet.as_view(), name= "login"),
     url('api/logout', LogoutViewSet.as_view(), name= "logout"),
     url('api/getVoter', GetVoterByUserType.as_view(), name= "getVoter"),
      url('api/updateVoter', UpdateVoter.as_view(), name= "updateVoter"),
      url('api/updateVoter/(?P<id>[0-9])/$', UpdateVoter.as_view(), name= "updateVoter"),
    # url('login_form/', LoginView.as_view(template_name='webservice_again/login.html'), name= "login_form")

]