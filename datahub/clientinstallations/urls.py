from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('client/<int:pk>/', views.client_detail.as_view(), name='client'),
    path('app/<int:pk>/', views.app_detail.as_view(), name='app'),
    path('server/<int:pk>/', views.server_detail.as_view(), name='server'),
    path('servers/', views.servers, name='servers'),
    path('servergroup/<int:pk>/', views.servergroup_detail.as_view(), name='servergroup'),
    path('servergroups/', views.servergroups, name='servergroups')

]