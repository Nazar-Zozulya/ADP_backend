from rest_framework import serializers
from user_app.serializers import StudentSerializer, UserSerializer
from .models import Course
from django.contrib.auth import get_user_model

User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    students = StudentSerializer(many=True)
    
    
    image = serializers.SerializerMethodField()
        
    class Meta:
        model = Course
        fields = ['id','image','name','description','author','students']
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return f'http://localhost:8000{obj.image.url}'
        return None