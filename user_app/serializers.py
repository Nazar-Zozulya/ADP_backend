from ADP_backend import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id','name','surname','email','image']
        
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url) if request else image_url
        return None


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','name','surname','email','password']
        extra_kwargs = { 'password' : { "write_only" : True } }
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data.get('name', ''),
            surname=validated_data.get('surname', ''))
        return user