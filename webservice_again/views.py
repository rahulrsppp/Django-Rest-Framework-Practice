from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from webservice_again.serializers import CheckUserExistenceSerializers


# @csrf_exempt
# @api_view(["GET"])
# class CheckUserExistence(API):
#
#     userLogout = UserLogoutSerializers()
#
#
#     def get
#
#     if userLogout.is_valid(raise_exception=False):
#
#         token = userLogout.validated_data['token']
#
#         if token:
#          data = {'message': 'Accessed Successfully'}
#
#          return Response(data, status=HTTP_200_OK)

