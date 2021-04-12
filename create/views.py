from django.shortcuts import render
from .forms import AllForm
from .models import item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


def creation_at(request):
    return render(request, 'create_chef_at.html', {'OFId': 1003211})


def creation_dem(request):
    # if request.method == "POST":
    print(request.method)
    form: AllForm = AllForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    items = item.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 10)
    try:
        item_list = paginator.page(page)
    except PageNotAnInteger:
        item_list = paginator.page(1)
    except EmptyPage:
        item_list = paginator.page(paginator.num_pages)
    return render(request, 'create_demand.html', {'item_list': item_list, 'OFId': 1003211, 'form': form})


def view_mo(request):
    return render(request, 'view_mo.html')


def Tasks(request):
    return render(request, 'Tasks.html')


def Validation(request):
    return render(request, 'validation_cycle.html')

def Machines(request):
    return render(request, 'Machines.html')


