from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_doc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),

    path('', include('profiles.urls')),
]

# urls для swagger
urlpatterns += yasg_doc
