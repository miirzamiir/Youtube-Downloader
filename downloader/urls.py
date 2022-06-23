from django.urls import path
from .views import Downloader

urlpatterns = [
    path('', Downloader.as_view(), name='index')
]