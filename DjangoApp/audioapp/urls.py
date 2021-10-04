# DjangoApp/audioapp/urls.py

from django.urls import path
from audioapp import views

app_name = 'audioapp'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]