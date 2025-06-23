from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='participants/', blank=True, null=True)

    def __str__(self):
        return self.name

    def initial(self):
        return self.name[0].upper()