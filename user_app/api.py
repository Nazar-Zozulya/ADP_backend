from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer

    # permission_classes = [AllowAny]
    # serializer_class = LoginSerializer

    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']

    #     login(request, user)

    #     # Создаём токен через Knox
    #     response = super().post(request)

    #     # Достаём токен из response
    #     token = response.data.get('token')
    #     expiry = response.data.get('expiry')

    #     # Сериализуем пользователя
    #     user_data = UserSerializer(user, context={'request': request}).data

    #     # Возвращаем полный ответ с токеном и данными пользователя
    #     return Response({
    #         "token": token,
    #         "expiry": expiry,
    #         "user": user_data,
    #     })


class RegisterAPI(generics.GenericAPIView):
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
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data
        return Response({
            "status": "success",
            "data": AuthToken.objects.create(user)[1]
        })
        # return Response({ "user": UserSerializer(user, context=self.get_serializer_context()).data,
        #                  "token": AuthToken.objects.create(user)[1] })


class UserAPI(generics.RetrieveAPIView):
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

# class ProfileAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user, context={'request': request})
#         return Response(serializer.data)