from musicapp.views import SongListApiView, ArtisteListApiView, LyricListApiView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'artist', ArtisteListApiView)
router.register(r'song', SongListApiView)
router.register(r'lyric', LyricListApiView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('music', include('musicapp.urls')),

]
