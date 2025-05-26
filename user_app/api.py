from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer

class RegisterAPI(generics.GenericAPIView):
    """ API регистрации """
    
    serializer_class=RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        return Response({
            "status": "success",
            "data": AuthToken.objects.create(user)[1]
        })
        

class LoginAPI(generics.GenericAPIView):
    """ API авторизации """

    
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        return Response({
            "status": "success",
            "data": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    """ API получения пользователя """
    

    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response({
            "status": "success",
            "data": serializer.data
        })