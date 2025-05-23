from rest_framework import serializers
from user_app.serializers import UserSerializer
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return f'http://localhost:8000{obj.image.url}'
        return None