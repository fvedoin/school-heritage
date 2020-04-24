from django import template

register = template.Library()


@register.filter(name='get_role')
def get_role(value):
    if value == 1:
        return 'diretor'
    elif value == 2:
        return 'professor'
    elif value == 3:
        return 'aluno'
