from django.db import models

from rooms.models import Room


class ItemManager(models.Manager):
    def with_num_problems_unsolved(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                        select i.id, i.name, i.description, i.room_id, COALESCE(tab_aux.num_problems, 0) as num_problems_unsolved
                        from items_item i left join (select count(*) as num_problems, item_id from problems_problem p where p.status = 0 group by item_id) as tab_aux
                        on i.id = tab_aux.item_id""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], name=row[1], description=row[2], room=Room.objects.get(pk=row[3]))
                p.num_problems_unsolved = row[4]
                result_list.append(p)
        return result_list

    def count_items_with_problems_unsolved(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                    select count(*)
                    from items_item i left join (select count(*) as num_problems_unsolved, item_id from problems_problem p where p.status = 0 group by item_id) as tab_aux_unsolved
                    on i.id = tab_aux_unsolved.item_id
                    where num_problems_unsolved > 0    
                            """)
            num = cursor.fetchone()
        return num[0]

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
    objects = ItemManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
