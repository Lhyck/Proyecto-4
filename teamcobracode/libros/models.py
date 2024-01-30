from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    # Opciones para el campo genero
    GENERO_CHOICES = [
        ('Aventura', 'Aventura'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Drama', 'Drama'),
        ('Fantasía', 'Fantasía'),
        ('Misterio', 'Misterio'),
    ]

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, verbose_name="Título")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    ISBN = models.CharField(max_length=150, verbose_name="ISBN")
    numDeInventario = models.IntegerField(verbose_name="Número de Inventario", default=0)
    descripcion = models.CharField(max_length=300, verbose_name="Descripción", default="")
    genero = models.CharField(max_length=100, verbose_name="Género", choices=GENERO_CHOICES, default="")
    estado = models.BooleanField(verbose_name="Disponibilidad", default=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="libros", default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    libroAlquilado = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nota = models.CharField(max_length=150, verbose_name="Nota", default="")

    class Meta:
        verbose_name = "registro"
        verbose_name_plural = "registros"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.usuario.username} - {self.libroAlquilado.titulo} - {self.libroAlquilado.autor}"
