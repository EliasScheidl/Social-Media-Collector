from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('', views.feed, name='feed'),
    path('view/', views.viewPost, name='view'),
    path('upload/', views.upload, name='upload'),
    path('reports/', views.manageReportedPost, name='reports'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)