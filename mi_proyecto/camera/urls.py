from django.urls import path
from . import views
from .views import camera_view

urlpatterns = [
    path('', views.index, name='index'),
    path('camera/', camera_view, name='camera'),
    # Agrega más URLs según sea necesario
]