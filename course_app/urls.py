from django.urls import path, include

from course_app.api import CourseDetailAPI, CourseListAPI


urlpatterns = [
    path('api/courses/all', CourseListAPI.as_view()),
    path('api/courses/<int:pk>', CourseDetailAPI.as_view()),
]