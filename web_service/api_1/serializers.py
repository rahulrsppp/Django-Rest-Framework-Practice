from django.contrib.auth.models import User
from rest_framework import serializers
from web_service.models import MyRudModel



class MyRudSerializers(serializers.ModelSerializer):


    class Meta:
        model= MyRudModel
        fields =( 'pk','title','user','time', 'content')

        # This is for the case if you don't want to update and create any fields.
        # User can not use the fields which are marked read only. If he/she tries to do so,
        # BAD REQUEST error will be shown.
        read_only_fields=('user',)

    ## this method is for validating title. We can makre more ethods from variable like validate_user, validate_time
    # Basic purpose is to avoid duplicacy of content
    def validate_title(self, value):
        val= MyRudModel.objects.filter(title__iexact=value)

        if val.exists():
            raise serializers.ValidationError("Duplicate Title")
        return value


class UserRegistrationSerializer(serializers.ModelSerializer):

    user_password = serializers.CharField(source='password', style={'input_style' : 'password'})

    class Meta:
        model = User
        fields= {'first_name', 'last_name', 'email', 'user_password'}


        def create(self, validated_data):
            user = User.Objects.create(**validated_data)
            user.set_password(user.password)
            user.save()
            return user