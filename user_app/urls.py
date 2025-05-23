from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
# , ProfileAPI
from knox import views as know_views


urlpatterns = [
    path('/', include('knox.urls')),
    path('/register', RegisterAPI.as_view()),
    path('/login', LoginAPI.as_view()),
    path('/user', UserAPI.as_view())
    # path('/profile', ProfileAPI.as_view()),
]