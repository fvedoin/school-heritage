from django import template

register = template.Library()


@register.filter(name='get_role')
def get_role(value):
    if value == 1:
        return 'Diretor'
    elif value == 2:
        return 'Professor'
    elif value == 3:
        return 'Aluno'
