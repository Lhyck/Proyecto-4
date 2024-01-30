from core import views
from libros import views as views_libros
from libros.views import (LibroListView, LibroCreate, LibroUpdate, LibroDelete, RegistroCreate)

from django.urls import path
from .views import exit

urlpatterns = [
    path('', views.index, name='index'),
    path('listado-libros/', LibroListView.as_view(), name='libros'),
    path('create-libro/', LibroCreate.as_view(), name='create'),
    path('create-registro/<int:pk>/', RegistroCreate.as_view(), name='createRegistro'),
    path('update-libro/<int:pk>/', LibroUpdate.as_view(), name='update'),
    path('delete-libro/<int:pk>/', LibroDelete.as_view(), name='delete'), 
    path('logout/', exit, name='exit'),
    path('contacto', views.contacto, name='contacto'),
    path('acercade', views.acercaDe, name='acerca'),
    path('alquilerLibro/', views_libros.alquilerLibros, name='alquilerLibros'),
    path('consultaLibro/', views_libros.consultarLibros, name='consultarLibros'),
    path('search/', views_libros.SearchResultView.as_view(), name='search'),
    path('searchRegistros/', views_libros.SearchResultViewRegistros.as_view(), name='searchRegistro'),
]
