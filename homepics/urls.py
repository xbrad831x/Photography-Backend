from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListHomepic.as_view())
]