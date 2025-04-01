from django.urls import path
from . import views

urlpatterns = [
    path('like/', views.like, name='like'),
    path('dislike/', views.like, name='dislike'),
    path('report/', views.like, name='report'),
    path('delete/', views.like, name='delete'),
]