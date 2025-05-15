from ADP_backend import settings
from rest_framework import serializers
from user_app.serializers import UserSerializer
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return f'http://localhost:8000{obj.image.url}'  # fallback если request нет
        return None