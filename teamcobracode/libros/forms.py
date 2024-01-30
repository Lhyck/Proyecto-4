from django import forms
from .models import Libro, Registro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'ISBN', 'numDeInventario', 'descripcion', 'genero', 'estado', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'numDeInventario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Inventario'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': '',
            'autor': '',
            'ISBN': '',
            'numDeInventario': 'Número de Inventario',
            'descripcion': '',
            'genero': 'Género',
            'estado': 'Disponibilidad',
            'imagen': 'Imagen',
        }


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['usuario', 'libroAlquilado', 'nota']
        widgets = {
            'usuario': forms.HiddenInput(),
            'libroAlquilado': forms.Select(attrs={'class': 'form-control'}),
            'nota': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nota'}),
        }
        labels = {
            'usuario': 'Usuario',
            'libroAlquilado': 'Libro Alquilado',
            'nota': 'Nota',
        }
        


        