from course_app.serializers import CourseSerializer
from rest_framework import generics







class CoursesAPI(generics):
    queryset
    
    serializer_class=CourseSerializer
    
    # def get