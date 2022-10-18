from django.urls import path
from .views import ex02View

urlpatterns = [
    path("", ex02View, name="index"),
]