from django.db import models

from items.models import Item
from users.models import CustomUser


class Problem(models.Model):
    status = models.IntegerField(null=False, blank=False, default=0, verbose_name='Situação')
    description = models.TextField(
        'Descrição'
    )
    item = models.ForeignKey(
        Item, verbose_name='Item',
        on_delete=models.CASCADE, related_name='problems'
    )
    user = models.ForeignKey(
        CustomUser, verbose_name='Usuario',
        on_delete=models.CASCADE
    )

    def first_log(self):
        return self.logs.first()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
