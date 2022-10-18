from django.urls import path

from .views import ex03View

urlpatterns = [
    path('', ex03View, name='index'),
]