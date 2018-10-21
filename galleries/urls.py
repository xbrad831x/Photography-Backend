from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListGallery.as_view())
]