from django.contrib import admin
from django.urls import path
from .views import PhotoList

app_name="photography"
urlpatterns = [
    path('',PhotoList.as_view(),name="photography"),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)