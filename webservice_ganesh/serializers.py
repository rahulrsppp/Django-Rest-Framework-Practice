from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions

from webservice_again.model import Snippet, VoterList
from rest_framework.authtoken.models import Token


class MySnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('name', 'email', 'mobile',) # where all fields of model are needed, you can use exclude=() instead of fields

class FillVoterListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VoterList
        fields = ('name', 'email', 'mobile', 'city', 'type')

class RegistrationSerializers(serializers.HyperlinkedModelSerializer):
    user_password = serializers.CharField(label="Password", source="password", style= {"input_type":"password"})

    # class Meta:
    #     model = Registration
    #     fields = ('name', 'mobile', 'email', 'username', 'user_password')



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username','user_password')


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(user.password)
        user.save()
        Token.objects.create(user = user)
        return user

class AuthTokenSerializers(serializers.Serializer):
    username = serializers.CharField(label='username', allow_blank= False) #check allow_blank parameter of CharField, we can skip manually checking the values if submitted or not
    password = serializers.CharField(label='password', style={'input_type': 'password'}, allow_blank= False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # check  EMPTY credentials
        if username and password: # we can skip this by using allow_blank in CharField of serializer

            # check user exist
            userObject = User.objects.filter(username=username)

            if userObject:
                # check username and password correct
                user = authenticate(username=userObject[0].username, password=password)

                if user:
                    # check user is active
                    if not user.is_active:
                        message = ({'logging': 'User is not active'})
                        raise serializers.ValidationError(message, code='authorization')
                else:
                    message = ({'logging': 'Wrong Credentials.'})
                    raise serializers.ValidationError(message, code='authorization')

            else:
                message = ({'logging': 'User not exist'})
                raise serializers.ValidationError(message, code='authorization')
        else:
            if not username:
                message = ({'username': "Please enter username"}) # required in serializer

            if not password:
                message = ({'password': 'Please enter password'})  # required in serializer

            if not username and not password:  # required in serializer
                message = ({'logging': 'please enter username and password'})

                raise serializers.ValidationError(message, code='authorization')

        ## Will return user if Evrything gonna good.
        attrs['user'] = user
        return attrs

  # check this method also
    def validate(self, attrs):
      try:
        user = User.objects.get(username=attrs['username'])
      except User.DoesNotExist:
        raise serializers.ValidationError('username/password invalid')

      if user and not user.is_active:
        raise exceptions.ValidationError('inactive_account')

      user = authenticate(username=attrs['username'], password=attrs['password'])
      if not user:
        raise serializers.ValidationError("Invalid credentials.")
      attrs['user'] = user
      return attrs


class CheckUserExistenceSerializers(serializers.Serializer):
    token =   serializers.CharField(label="token")

    def validate(self, attrs):
       myToken =  attrs.get("token")
       print("::::::: TOKEN TO CHECK: ",myToken) 
       if myToken:

           verifiedToken = Token.objects.get(key= myToken) # raise validation error if token object not found

           if not verifiedToken:
               print("::::::: TOKEN NOT EXIST: ")

               msg = {"message": "Not Verified"}
               raise  serializers.ValidationError(msg, code="authorization")
           else: # extra block, not required

               print("::::::: TOKEN EXIST: ")


       else:
           print("::::::: WRONG TOKEN ")

           msg = {"message": "Wrong Token"}
           raise serializers.ValidationError(msg, code="authorization")

       attrs['token']=verifiedToken
       return attrs




