from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from webservice_again.model import Snippet, VoterList
from rest_framework.authtoken.models import Token


class MySnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('name', 'email', 'mobile',)

class AddVoterSerializers(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = VoterList
        fields = ('id','name', 'email', 'mobile', 'city', 'type')


    def update(self, instance, validated_data):
        print(":::::: Instance: ",instance)
        print(":::::: validated_data: ",validated_data)
        print(":::::: Instance Email: ", instance.email)

        instance.name = validated_data.pop("name", instance.name)
        instance.email = validated_data.pop("email", instance.email)
        instance.save()

        return  instance

    





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
    username = serializers.CharField(label='username')
    password = serializers.CharField(label='password', style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        # check  EMPTY credentials
        if username and password:

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
                message = ({'username': "Please enter username"})

            if not password:
                message = ({'password': 'Please enter password'})

            if not username and not password:
                message = ({'logging': 'please enter username and password'})

                raise serializers.ValidationError(message, code='authorization')

        ## Will return user if Evrything gonna good.
        attrs['user'] = user
        return attrs


class CheckUserExistenceSerializers(serializers.Serializer):
    token =   serializers.CharField(label="token")

    def validate(self, attrs):
        myToken =  attrs.get("token")
        print("::::::: TOKEN TO CHECK: ",myToken)
        if myToken:

            verifiedToken = Token.objects.get(key= myToken)

            if not verifiedToken:
                print("::::::: TOKEN NOT EXIST: ")

                msg = {"message": "Not Verified"}
                raise  serializers.ValidationError(msg, code="authorization")
            else:

                print("::::::: TOKEN EXIST: ")


        else:
            print("::::::: WRONG TOKEN ")

            msg = {"message": "Wrong Token"}
            raise serializers.ValidationError(msg, code="authorization")

        attrs['token']=verifiedToken
        return attrs

class GetUserListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





