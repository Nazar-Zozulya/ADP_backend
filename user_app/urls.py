from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
# , ProfileAPI
from knox import views as know_views


urlpatterns = [
    path('/', include('knox.urls')),
    path('api/users/register', RegisterAPI.as_view()),
    path('api/users/login', LoginAPI.as_view()),
    path('api/users/user', UserAPI.as_view()),
    path('api/users/logout', know_views.LogoutView.as_view()),
    # path('/profile', ProfileAPI.as_view()),
]