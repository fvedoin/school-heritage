from django.db import models

from items.models import Item
from users.models import CustomUser


class ProblemManager(models.Manager):
    def num_problems_created(self, initial_date, final_date):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                        select count(*)
                        from problems_problem p join (select l.problem_id, min(date(l.date)) as first_date from logs_log l group by l.problem_id) problem_log
                        on p.id = problem_log.problem_id
                        where problem_log.first_date between %s and %s
                      """, [initial_date, final_date])
            num = cursor.fetchone()
        return num[0]

    def num_problems_resolved(self, initial_date, final_date):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                        select count(*)
                        from problems_problem p join (select l.problem_id, max(date(l.date)) as last_date from logs_log l group by l.problem_id) problem_log
                        on p.id = problem_log.problem_id and p.status = 1
                        where problem_log.last_date between %s and %s
                             """, [initial_date, final_date])
            num = cursor.fetchone()
        return num[0]


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
    objects = ProblemManager()

    def first_log(self):
        return self.logs.first()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
