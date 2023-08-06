# views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()

from django.shortcuts import render


def render_registration(request):
    return render(request, 'registration/register.html')


def render_login(request):
    return render(request, 'registration/login.html')


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email_phone = serializer.validated_data['email_phone']
            password = serializer.validated_data['password']

            # Аутентификация по email или phone
            user = None
            try:
                user = User.objects.get(username=email_phone)
            except User.DoesNotExist:
                pass

            if not user:
                try:
                    user = User.objects.get(phone=email_phone)
                except User.DoesNotExist:
                    pass

            if not user:
                return Response({'error': 'Invalid email/phone or password.'}, status=status.HTTP_401_UNAUTHORIZED)

            user = authenticate(username=user.username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email/phone or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
