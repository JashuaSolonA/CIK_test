from django.urls import path
from . import views

urlpatterns = [
    path('', views.enviar_db, name="main"),
    path('obtener_ultimo_dato/', views.obtener_ultimo_dato, name='obtener_ultimo_dato'),
]
