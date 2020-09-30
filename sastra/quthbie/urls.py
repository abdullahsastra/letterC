from django.urls import path
from quthbie import views

urlpatterns = [
    path('', views.satuIndex, name='satuIndex'),
    path('login', views.loginIndex, name='loginIndex'),
]