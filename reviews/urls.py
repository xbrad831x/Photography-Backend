from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListReview.as_view())
]