from django.db import models

from rooms.models import Room

class Item(models.Model):
    name = models.CharField(
        'Nome', max_length=100, unique=True
    )
    description = models.TextField(
        'Descrição'
    )
    room = models.ForeignKey(
        Room, verbose_name='Sala',
        on_delete=models.CASCADE, related_name='items'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'