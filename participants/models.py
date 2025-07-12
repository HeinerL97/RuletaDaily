from django.db import models 
from proyecto.models import Proyecto

class Participant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='participants/', blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return self.name

    def initial(self):
        return self.name[0].upper()

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()  # o .title(), o .upper()
        super().save(*args, **kwargs)
