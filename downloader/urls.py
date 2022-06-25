from django.urls import path
from .views import Audio, Downloader, HighQualityVideo, LowQualityVideo

urlpatterns = [
    path('', Downloader.as_view(), name='index'),
    path('audio/<str:id>', Audio.as_view(), name='audio'),
    path('low/<str:id>', LowQualityVideo.as_view(), name='low_vid'),
    path('high/<str:id>', HighQualityVideo.as_view(), name='high_vid'),
    
]