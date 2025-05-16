import json
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import CustomUser
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate


User = get_user_model()

# Create your views here.


def success(data):
    return JsonResponse({"status":'success','data':data}, safe=False)

def error(message, code):
    return JsonResponse({"status":'error','message':message,'code': code}, safe=False)




# @require_POST
def register(request):
    if request.method == "POST":  
        data = json.loads(request.body)  
        email = data.get('email')
        name = data.get('name')
        surname = data.get('surname')
        password = data.get('password')
        
        
        if not all([email, name, surname, password]):
            return  error('Поля на введені', 400)
        
        try:
            validate_email(email)
        except ValidationError:
            return error('Неверний email', 400)
        
        if User.objects.filter(email=email).exists():
            return error('Пользовутель уже существует', 400)
        
        user = CustomUser.objects.create(
            email=email,
            name=name,
            surname=surname,
            # password=password,
        )
        
        user.set_password(password)  # ✅ безопасно — хеширует пароль
        user.save()
        
        token = default_token_generator.make_token(user)
        
        return success(token)
        
    return error('Метод не поддерживается', 405)

def login(request):
    if request.method == "POST":
        data = json.loads(request.body)  
        email = data.get('email')
        password = data.get('password')
        
        
        if not all([email, password]):
            return  error('Поля на введені', 400)
        
        try:
            validate_email(email)
        except ValidationError:
            return error('Неверний email', 400)

        user = authenticate(request, email=email, password=password)
        
        
        if user is None:
            return error('Неверный email или пароль', 401)

        if not user.is_active:
            return error('Аккаунт не активирован', 403)
        
        token = default_token_generator.make_token(user)
        
        return success(token)
        
    
    return error('Метод не поддерживается', 405)