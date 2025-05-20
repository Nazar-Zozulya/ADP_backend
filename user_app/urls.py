from django.urls import path, include
from .api import RegisterAPI
from knox import views as know_views


urlpatterns = [
    path('/', include('knox.urls')),
    path('/register', RegisterAPI.as_view()),
]