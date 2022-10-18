from django.urls import path
from .views import homePageView, ex00View

urlpatterns = [
    path("ex00", ex00View, name="markdown"),
]