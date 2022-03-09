from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    url("upimage", views.upimage, name="upimage")
]