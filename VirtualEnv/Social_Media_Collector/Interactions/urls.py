from django.urls import path
from . import views

app_name = "interact"

urlpatterns = [
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
    path('report/', views.report, name='report'),
    path('delete/', views.delete, name='delete'),
    path('auth/', views.authenticate, name='authenticate'),
    path('logout/', views.logoutUser, name='logout'),
    path('post/', views.post, name='post'),
]