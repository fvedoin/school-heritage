from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import schoolmaster_required
from items.models import Item
from problems.models import Problem

@login_required
@schoolmaster_required
def index(request):
    template_name = 'reports/index.html'
    num_items_with_problems = Item.objects.count_items_with_problems_unsolved()
    total_items = Item.objects.all().count()
    num_problems_unsolved = Problem.objects.filter(status=0).count()
    total_problems = Problem.objects.all().count()
    context = {
        'num_items_with_problems': num_items_with_problems,
        'num_problems_unsolved': num_problems_unsolved,
        'total_items': total_items,
        'total_problems': total_problems
    }
    return render(request, template_name, context)
