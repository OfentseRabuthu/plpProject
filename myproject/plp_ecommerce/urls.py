from django.urls import path
from .views import home

urlpatterns = [
    path('views/', home, name='home'),
    ]
   #  1. Add an import:  from my_app import views
   # 2. Add a URL to urlpatterns:  path('', views.home, name='home')