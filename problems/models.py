from django.db import models

from items.models import Item
from users.models import CustomUser

class Problem(models.Model):
    status = models.IntegerField(null=False,blank=False,default=0)
    description = models.TextField(
        'Descrição'
    )
    item = models.ForeignKey(
        Item, verbose_name='Item',
        on_delete=models.CASCADE
    )
    usuario = models.ForeignKey(
    		CustomUser, verbose_name='Usuario',
    		on_delete=models.CASCADE
    )


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
