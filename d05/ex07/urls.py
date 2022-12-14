from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.Init.as_view(), name='ex07-init'),
    path('populate/', views.Populate.as_view(), name='ex07-populate'),
    path('display/', views.Display.as_view(), name='ex07-display'),
    path('remove/', views.Remove.as_view(), name='ex07-remove'),
    path('update/', views.Update.as_view(), name='ex07-remove'),
]
