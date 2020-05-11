from django.db import models

from django.utils import timezone

from problems.models import Problem

class Log(models.Model):
    title = models.TextField('Título',blank=False,null=True)
    description = models.TextField('Descrição')
    date = models.DateTimeField(default=timezone.now)

    problem = models.ForeignKey(
        Problem, verbose_name='Problema',
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
