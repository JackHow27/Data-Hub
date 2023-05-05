from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('client/<int:pk>/', views.client_detail.as_view(), name='client')


]