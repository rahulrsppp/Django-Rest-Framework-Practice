from django.contrib.auth.models import User
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK

from webservice_again.model import Snippet, VoterList
from webservice_again.serializers import MySnippetSerializer, AuthTokenSerializers, RegistrationSerializers, \
    CheckUserExistenceSerializers, AddVoterSerializers
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout

class MySnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = MySnippetSerializer

    def list(self, request, *args, **kwargs):
        queryset = Snippet.objects.all()
        serializer_class = MySnippetSerializer(queryset, many=True)

        return Response(serializer_class.data) #send http status code in the response also.

    @action(methods=['get'], detail=True)
    def newest(self, request):
        newest = self.get_queryset().order_by('name').last()
        serializer = self.get_serializer_class()(newest)
        return Response({'response': serializer.data,
                         'message_received': "Success"})

    @action(methods=['get'], detail=False, url_path="getalldata", url_name="getalldata")
    def getAll(self, request):
        allData = self.get_queryset().order_by('email').last()

        serializer_class = self.get_serializer_class()(allData) #??? get_serializer_class(allData)

        return Response({"response_data": serializer_class.data,
                         "message": "Successful"})


class RegistrationViewset(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializers
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        myData = self.serializer_class(data=request.data)

        if myData.is_valid(raise_exception=True): #naming convention, use variable and other names according to PEP8 
            register = myData.save()

            return Response({"message": "Registered Successfully",
                             "status": status.HTTP_201_CREATED,
                             })


class LoginViewSet(APIView):
    serializer_class = AuthTokenSerializers


    def post(self, request, *args, **kwargs):

        # validating data in the AuthTokenSerializers
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # fetching User info from AuthTokenSerializers
            user = serializer.validated_data['user']
            # line 73 to 80
            # you first deleted the auth_toekn and using get_or_create

            try:
                user.auth_token.delete()
            except Exception as e:
                pass

            # creating new token
            token, created = Token.objects.get_or_create(user=user) 

            return Response({'status': status.HTTP_200_OK,
                             'token': token.key,
                             'message': 'LoggedIn Successfully',

                             })

        else: #I think this block is unreachable as raise_exception = True, test this else block
            return Response({
                "message": 'Invalid Request.'
            })

class LogoutViewSet(APIView):


    def get(self, request, *args,**kwargs):
        request.user.user_token.delete()

        return Response({
            "message": 'Logout Successful'
        }) # Http staus code


class CheckUserExistence(APIView):


    def post(self, request, *args,**kwargs):
        # print("::::::: Back Token: ", request.data)
        # token = Token.objects.get(key=request.data['token'])
        # print("::::::: Token: ", token)
        # print("::::::: created: ", token.created)
        #
        # data = {'message': 'Accessed Successfully',
        #         'token':token.key,
        #         'id': token.user_id}
        #
        # return Response(data, status=HTTP_200_OK)

        serializer = CheckUserExistenceSerializers(data=request.data)

        if serializer.is_valid(raise_exception=False):

            token = serializer.validated_data['token']

            if token and token.user_id:

              user = User.objects.get(id=token.user_id)

              if user:
                  if user.is_staff == 1:

                      data = {'message': 'Accessed Successfully',
                              'password': user.password,
                              'token': token.key,
                              'id': token.user_id}

                      return Response(data, status=HTTP_200_OK)
                  else:
                      return Response({
                          "message": 'Chal Lodu..'
                      })
              else:
                  return Response({
                      "message": 'Chal Bhosadi K..'
                  })

        else:
            return Response({
                "message": 'Invalid Request.'
            })

class FillVoterListViewSet(viewsets.ModelViewSet):

    serializer_class =  AddVoterSerializers

    def create(self, request, *args, **kwargs):

        serializable = self.serializer_class(data=request.data)
        isValid = serializable.is_valid(raise_exception = True)

        if isValid: # what if not valid?
            serializable.save()

            return Response({
                    "message": 'Saved Successfully'
                })



class GetVoterByUserType(APIView):

    serializer_class =  AddVoterSerializers
    permission_classes = (IsAuthenticated,)

    # def list(self, request, *args, **kwargs):
    #     # list = VoterList.Objects.all()
    #     serializable =  self.serializer_class(list, many=True)
    #     return Response({
    #         "voter_list": fullList.data
    #
    #     })

    def get(self, request,*args,**kwargs):
        list = VoterList.objects.all() #list is a keyword in python, can't use it as variable name
        listData = self.serializer_class(list, many=True)

        return Response({
            "voter_list": listData.data

        })