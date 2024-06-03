from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios_list, name='usuarios_list'),
    path('new/', views.usuarios_create, name='usuarios_new'),
    path('edit/<int:pk>/', views.usuarios_update, name='usuarios_edit'),
    path('delete/<int:pk>/', views.usuarios_delete, name='usuarios_delete'),
]
