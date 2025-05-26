from course_app.models import Course
from course_app.serializers import CourseSerializer
from rest_framework import generics
from rest_framework.response import Response







class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    
    serializer_class=CourseSerializer
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "status": "success",
                "data": serializer.data
            })
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            })
    
    
class CourseDetailAPI(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                "status": "success",
                "data": serializer.data
            })
        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            })