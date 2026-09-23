from django.urls import path
from .views import index, usuarioContato, cadContato, altContato, excContato

urlpatterns = [
    path('', index, name='index'),
    path('usuario/<int:pk>', usuarioContato, name="usuario"),
    path('cadContato', cadContato, name="cadContato"),
    path('altContato/<int:pk>', altContato, name="altContato"),
    path('excContato/<int:pk>', excContato, name="excContato"),
]