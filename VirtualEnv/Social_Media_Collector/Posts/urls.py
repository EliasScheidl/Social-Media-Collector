from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.feed, name='feed'),
    path('view/', views.viewPost, name='view'),
    path('upload/', views.upload, name='upload'),
    path('reports/', views.manageReportedPost, name='reports'),
]