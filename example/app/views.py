from django.http import HttpResponse
from django.shortcuts import render
from modal_forms import ModalForm
from . import models, forms

def get_form_data(request, name, pk=None):
    form = getattr(forms, name)()
    mf = ModalForm(form, request, pk)
    mf.date_format = "%Y-%m-%d"
    data = mf.serialize_form()
    return HttpResponse(data)

def index(request):
    return render(request, 'app/index.html', {})

# EXAMPLES

def basic_example(request, bs_version):
    companies = models.Company.objects.all().order_by('name')
    consoles = models.Console.objects.all().order_by('company__name', 'name')
    invalid_form = None
    
    page_forms = {
        'company': forms.CompanyForm(auto_id="CompanyForm_%s"),
        'console': forms.ConsoleForm(auto_id="ConsoleForm_%s"),
        'game': forms.GameForm(auto_id="GameForm_%s"),
    }
    
    # handle form submission
    if request.POST:
        name = request.POST.get('mf-name', None)
        pk = request.POST.get('mf-pk', None)

        mf = ModalForm(page_forms[name], request, pk)
        page_forms[name], invalid_form = mf.process_form()

    context = {
        'forms': page_forms,
        'invalid_form': invalid_form,
        'companies': companies,
        'consoles': consoles,
    }

    return render(request, 'app/bootstrap{}/basic.html'.format(bs_version), context)

def datatables(request, bs_version):
    games = models.Game.objects.all()
    invalid_form = None

    page_forms = {
        'game': forms.GameForm(auto_id="GameForm_%s"),
    }
    
    # handle form submission
    if request.POST:
        name = request.POST.get('mf-name', None)
        pk = request.POST.get('mf-pk', None)

        mf = ModalForm(page_forms[name], request, pk)
        page_forms[name], invalid_form = mf.process_form()

    context = {
        'forms': page_forms,
        'invalid_form': invalid_form,
        'games': games,
    }

    return render(request, 'app/bootstrap{}/datatables.html'.format(bs_version), context)
