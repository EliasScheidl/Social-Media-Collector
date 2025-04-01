from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('view/', views.viewPost, name='view'),
    path('upload/', views.upload, name='upload'),
    path('reports/', views.upload, name='reports'),
]