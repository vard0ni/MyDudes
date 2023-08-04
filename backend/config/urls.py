from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_doc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/',   include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# urls для swagger
urlpatterns += yasg_doc
