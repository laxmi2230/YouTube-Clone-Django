from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from videos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('videos/', include('videos.urls', namespace="videos")),
    path('<str:username>/', views.profile, name='profile'),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
