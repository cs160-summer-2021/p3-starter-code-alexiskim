from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('pencil_brush', views.pencil_brush, name='pencil_brush'),
    path('flat_brush', views.flat_brush, name='flat_brush'),
    path('bucket', views.bucket, name='bucket'),
    path('drawing_screen', views.drawing_screen, name='drawing_screen'),
    path('home', views.home, name='home')
]
