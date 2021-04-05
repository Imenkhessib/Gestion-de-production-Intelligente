from django.shortcuts import render
from .forms import AllForm
from .models import piece
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


def creation_at(request):
    return render(request, 'create_chef_at.html', {'OFId': 1003211})


def creation_dem(request):
    # if request.method == "POST":
    print(request.method)
    form: AllForm = AllForm(request.POST)
    print(form.errors)
    if form.is_valid():
        aa = form.cleaned_data['product_id']
        bb = form.cleaned_data['designation']
        cc = form.cleaned_data['quantity']
        form.save()
    pieces = piece.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(pieces, 10)
    try:
        piece_list = paginator.page(page)
    except PageNotAnInteger:
        piece_list = paginator.page(1)
    except EmptyPage:
        piece_list = paginator.page(paginator.num_pages)
    return render(request, 'create_demand.html', {'piece_list': piece_list,'OFId': 1003211, 'form': form})


def creation_dem1(request):
    if request.method == "POST":
        qty = request.POST["quantity"]
        ref = request.POST["ref"]
        desig = request.POST["desig"]

        return render(request, 'create_demand.html', {'OFId': 1003211, 'qty': qty, 'ref': ref, 'desig': desig})

    else:
        return piece_detail(request)

def view_mo(request):
    return render(request, 'view_mo.html')


def edit_dem(request):
    return render(request, 'edit_demand.html', {'OFId': 1003211})


def edit_prod(request):
    return render(request, 'edit_resp_prod.html', {'OFId': 1003211})


def edit_at(request):
    return render(request, 'edit_at.html', {'OFId': 1003211})


def Tasks(request):
    return render(request, 'Tasks.html')


def piece_detail(request):
    template_name = "create_demand.html"
    pieces = piece.objects.all()

    context = {'pieces': pieces}
    resp = render(request, template_name, context)
    return resp


