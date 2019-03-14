from rest_framework import routers

from webservice_again.testviewset import ListRetrieveViewSet
from webservice_again.viewset import (
    MySnippetViewSet, RegistrationViewset, CheckUserExistence, LoginViewSet,
    AddVoterViewSet, GetVoterByUserType,
    UpdateVoter)


myRouters = routers.DefaultRouter()
myRouters.register('snippets', MySnippetViewSet, base_name='snippets')
myRouters.register('register', RegistrationViewset, base_name='registration')
myRouters.register('fillVoter', AddVoterViewSet, base_name='fillVoter')
# myRouters.register('getVoter', GetVoterByUserType, base_name='getVoter')


