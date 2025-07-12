from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.capitalize()  # O usa title() o upper() según prefieras
        super().save(*args, **kwargs)