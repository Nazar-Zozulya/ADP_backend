from django.shortcuts import render
from .models import Course, Lesson, Test, AnswerOption
from .serializers import CourseSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def success(data):
    return JsonResponse({"status":'success','data':data}, safe=False)

def error(message):
    return JsonResponse({"status":'error','message':message}, safe=False)

@api_view(['GET'])
def get_all(request):
    try:
        all_courses = Course.objects.all()
        
        serialized_courses = CourseSerializer(all_courses, many=True).data
        
        return success(serialized_courses)
    except:
        return error('loading courses error')
    