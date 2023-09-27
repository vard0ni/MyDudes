from django.urls import path
from .views import RegistrationView, LoginView, render_registration, render_login

urlpatterns = [
    path('register/', render_registration, name='render_registration'),
    path('login/', render_login, name='render_login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]