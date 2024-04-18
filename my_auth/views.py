from django.http import HttpRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import BasicUser
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.shortcuts import render

# Добавьте эту функцию
def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request: HttpRequest):
    user_serializer = UserRegistrationSerializer(data=request.data)
    if user_serializer.is_valid():
        # Проверка значения role
        role = user_serializer.validated_data.get('role')
        if role not in ['Линкольн', 'Дуглас', 'Lincoln', 'Duoglas']:
            return Response({'error': 'Некорректное значение для поля role. Допустимые значения: "Линкольн", "Дуглас".'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Проверка на существование пользователя с таким же email или username
        email = user_serializer.validated_data.get('email')
        username = user_serializer.validated_data.get('name')
        if BasicUser.objects.filter(email=email).exists():
            return Response({'error': 'Пользователь с таким email уже существует.'}, status=status.HTTP_400_BAD_REQUEST)
        if BasicUser.objects.filter(username=username).exists():
            return Response({'error': 'Пользователь с таким именем пользователя уже существует.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Создание пользователя с помощью модели BasicUser
            user = BasicUser.objects.create(
                username=username,
                email=email,
                password=make_password(user_serializer.validated_data['password']),  # Хеширование пароля
                role=role
            )
            user.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)