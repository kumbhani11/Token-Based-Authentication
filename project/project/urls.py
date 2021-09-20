
from django.contrib import admin
from django.urls import path
from application.views import *


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/users/', Users.as_view()),
    path('admin/', admin.site.urls),
    path('api/login2/', Login2API.as_view()),

    
]
