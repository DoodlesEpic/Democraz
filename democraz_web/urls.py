from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<int:pagina>', views.inicio, name='inicio'),
    path('detalhes/<int:pec>', views.detalhes, name='detalhes'),
]
