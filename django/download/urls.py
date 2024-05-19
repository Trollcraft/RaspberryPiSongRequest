from django.urls import path
from . import views
# /api/
urlpatterns = [
    path("download/", views.download),
    path("showPlaylist/", views.showPlaylist),
    path("play/", views.playing)
]
