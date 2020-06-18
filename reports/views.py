from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import schoolmaster_required
from items.models import Item
from problems.models import Problem
from logs.models import Log
from datetime import datetime
import json
from django.http import HttpResponse


@login_required
@schoolmaster_required
def index(request):
    template_name = 'reports/index.html'
    num_items_with_problems = Item.objects.count_items_with_problems_unsolved()
    total_items = Item.objects.all().count()
    num_problems_unsolved = Problem.objects.filter(status=0).count()
    total_problems = Problem.objects.all().count()
    data_inicio_mes = datetime.today().replace(day=1)
    data_hoje = datetime.today()
    num_problems_created = Problem.objects.num_problems_created(initial_date=data_inicio_mes.date(),
                                                                final_date=data_hoje.date())
    num_problems_resolved = Problem.objects.num_problems_resolved(initial_date=data_inicio_mes.date(),
                                                                  final_date=data_hoje.date())
    context = {
        'num_items_with_problems': num_items_with_problems,
        'num_problems_unsolved': num_problems_unsolved,
        'total_items': total_items,
        'total_problems': total_problems,
        'data_inicio_mes': data_inicio_mes,
        'data_hoje': data_hoje,
        'num_problems_created': num_problems_created,
        'num_problems_resolved': num_problems_resolved
    }
    return render(request, template_name, context)


def searchProblemsCreated(request):
    if request.is_ajax():
        initial_date = request.GET.get('initial_date')
        final_date = request.GET.get('final_date')
        try:
            initial_date = datetime.strptime(initial_date, '%d/%m/%Y')
            final_date = datetime.strptime(final_date, '%d/%m/%Y')
            if final_date >= initial_date:
                num_problems_created = Problem.objects.num_problems_created(initial_date=initial_date.date(),
                                                                            final_date=final_date.date())
                data = {'success': True, 'message': num_problems_created}
            else:
                data = {'success': False, 'message': 'Datas inválidas'}
        except:
            data = {'success': False, 'message': 'Datas inválidas'}
        return HttpResponse(json.dumps(data), content_type='application/json')


def searchProblemsResolved(request):
    if request.is_ajax():
        initial_date = request.GET.get('initial_date')
        final_date = request.GET.get('final_date')
        try:
            initial_date = datetime.strptime(initial_date, '%d/%m/%Y')
            final_date = datetime.strptime(final_date, '%d/%m/%Y')
            if final_date >= initial_date:
                num_problems_resolved = Problem.objects.num_problems_resolved(initial_date=initial_date.date(),
                                                                              final_date=final_date.date())
                data = {'success': True, 'message': num_problems_resolved}
            else:
                data = {'success': False, 'message': 'Datas inválidas'}
        except:
            data = {'success': False, 'message': 'Datas inválidas'}
        return HttpResponse(json.dumps(data), content_type='application/json')
