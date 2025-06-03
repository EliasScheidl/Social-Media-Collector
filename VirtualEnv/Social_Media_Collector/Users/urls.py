from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)