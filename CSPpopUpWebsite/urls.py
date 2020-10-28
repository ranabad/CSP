from django.urls import path
from . import views

urlpatterns = [
path('', views.mcq, name='mcq'),
]