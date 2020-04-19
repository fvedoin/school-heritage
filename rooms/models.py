from django.db import models

class Room(models.Model):
    name = models.CharField(
        'Nome', max_length=100, unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'