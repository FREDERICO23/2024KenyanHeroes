from django.urls import path
from . import views

urlpatterns = [
    path('hero/create/', views.hero_create, name='hero_create'),
    path('', views.hero_list, name='hero_list'),
    path('hero/<int:pk>/', views.hero_detail, name='hero_detail'),
    path('hero/<int:pk>/update/', views.hero_update, name='hero_update'),
    path('hero/<int:pk>/delete/', views.hero_delete, name='hero_delete'),
]