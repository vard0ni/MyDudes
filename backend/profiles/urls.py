from django.urls import path
from . import views


urlpatterns = [
    # для GET запросов выполнится функция 'retrieve', а для PUT запросов - 'update
    path('profile/<int:pk>/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    # этот путь будет реагировать только на GET запросы, выполняя функцию 'retrieve' в этом случае
    path('<int:pk>/', views.UserPublicView.as_view({'get': 'retrieve'})),
]