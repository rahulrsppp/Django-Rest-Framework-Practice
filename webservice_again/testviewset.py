from rest_framework import viewsets, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from webservice_again.model import VoterList
from webservice_again.serializers import AddVoterSerializers


class ListRetrieveViewSet(viewsets.ModelViewSet):

    serializer_class =  AddVoterSerializers
    authentication_classes = (TokenAuthentication,)

    def list(self,request):
        print("::::: List")
        validatedData = self.serializer_class(VoterList.objects.all().order_by("-id"), many=True)


        return Response ({'data': validatedData.data})

    def retrieve(self,request , pk=None):
        print("::::: Retrieve")
        singleVoter = VoterList.objects.get(pk=pk)

        if singleVoter is not None:
            validatedData = self.serializer_class(singleVoter)

            return Response({'data': validatedData.data})
        else:
            return Response({'message': "No Data"})


    def create(self, request):
        print("::::: Create")

        return


'''
This Update will work if the User hit api of PUT type, with PATH param and body param as well.
'''
def update(self, request, pk=None):
    print("::::: Update")

    isDataExist = VoterList.objects.get(id=pk)

    if not isDataExist:
        return Response({"message": "No Voter exist with this id."})
    else:

        '''  If Partial=True, that means there is no need to send all fields data for updation, user can send that
        field data which he want to update. This case will only applicable if user doesn't marked all fields mandatory.
        , At Partial=False, User have to send all fields data for updation'''
        isDataUpdated = self.serializer_class(isDataExist, request.data, partial=True)

        if isDataUpdated.is_valid():
            isDataUpdated.save()
            return Response({"message": "Voter updated."})
        else:
            return Response({"message": "All fields is Mandatory."})



def partial_update(self, request, pk=None):
    print("::::: Partial Update")


def destroy(self, request, pk=None):
    print("::::: Destroy")


