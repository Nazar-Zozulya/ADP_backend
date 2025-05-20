"""
URL configuration for ADP_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from ADP_backend import settings
from course_app import views as coruse_views
from user_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/all', coruse_views.get_all),
    path('api/users', include('user_app.urls')),
    # path('users/register', user_views.register),
    # path('users/login', user_views.login),
    # path('users/me', user_views.UserInfoView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 