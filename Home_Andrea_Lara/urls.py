from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('genero_animacion/', views.vista_animacion, name = 'vista_animacion'),
    path('genero_comedia/', views.vista_comedia, name = 'vista_comedia')
]