from django.shortcuts import render
from .models import Course, Lesson, Test, AnswerOption
from .serializers import CourseSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_GET

# Create your views here.
def success(data):
    return JsonResponse({"status":'success','data':data}, safe=False)

def error(message):
    return JsonResponse({"status":'error','message':message}, safe=False)

@require_GET
def get_all(request):
    try:
        all_courses = Course.objects.all()
        
        serialized_courses = CourseSerializer(all_courses, many=True).data
        
        return success(serialized_courses)
    except:
        return error('loading courses error')
    