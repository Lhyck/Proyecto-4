from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Libro, Registro
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from libros.forms import LibroForm, RegistroForm
from django.views.generic.list import ListView
from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db.models import Q

class LibroListView(ListView):    
    model = Libro

class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('libros')

class RegistroCreate(CreateView):
    model = Registro
    # fields = ['usuario', 'nota', 'libroAlquilado']
    form_class = RegistroForm
    success_url = reverse_lazy('index')
    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            print(self.request)
            kwargs['initial'] = {'libroAlquilado': self.kwargs['pk'], 'usuario': self.request.user}
            return kwargs

    def form_valid(self, form):
        # Asigna el valor de libro_id al campo libroAlquilado antes de guardar el formulario
        form.instance.libroAlquilado = get_object_or_404(Libro, id=self.kwargs['pk'])
        # Asegúrate de que el campo usuario tenga un valor antes de validar el formulario
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('libros')+'?Actualizado'
    
class LibroDelete(DeleteView):
    model = Libro
    def get_success_url(self):
        return reverse_lazy('libros')+'?Eliminado'

class SearchResultView(generic.ListView):
    model = Libro
    template_name = "libros/buscados.html"

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        libro_list = Libro.objects.filter(
            Q(autor__icontains=query) | Q(titulo__icontains=query)
        ).distinct()
        return libro_list

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

class SearchResultViewRegistros(generic.ListView):
    model = Registro
    template_name = "libros/registrosBuscados.html"

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        prestamo_list = Registro.objects.filter(
            Q(usuario__username__icontains=query) | Q(libroAlquilado__titulo__icontains=query)
        ).distinct()
        return prestamo_list
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['registro_list'] = self.get_queryset() 
        return context

# Create your views here.
@login_required
def alquilerLibros(request):
    print(request.user, "REQUEST USER")
    libros=Libro.objects.all()
    return render(request,"libros/alquilerLibro.html", {"mislibros":libros})

def consultarLibros(request):
    libros=Libro.objects.all()
    return render(request,"libros/consultarLibros.html", {"mislibros":libros})  

