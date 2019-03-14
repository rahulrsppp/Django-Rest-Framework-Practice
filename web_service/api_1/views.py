from rest_framework import  generics
from web_service.models import MyRudModel
from .serializers import MyRudSerializers


# For Showing Data list with queryset (method or variable).
# If developer want to perform CRUD operations, He/She need to call methods of CRUD.
class MyPostApiOperations(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = MyRudSerializers

    # required if want to fetch complete data from the DB. (In our case this, method will work for ListApiView Case)
    # We can also use 'queryset' variable in place of 'get_queryset' fun.
    def get_queryset(self):
        print("++++++++++++++++++++++++++++++++++ 0")
        return MyRudModel.objects.all()

    def post(self,request,*args,**kwargs):
        return #



class MyRudOperations(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MyRudSerializers

    def get_queryset(self):
        return MyRudModel.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return MyRudModel.objects.get(pk)

# FOR POST ONLY
class PostOnlyApiOperations(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = MyRudSerializers


