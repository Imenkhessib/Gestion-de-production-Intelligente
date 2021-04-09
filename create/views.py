from django.shortcuts import render, redirect
from .forms import AllForm, essai, MO_form, formm
from .models import piece,MO, project
from .filters import filterr, filterrr
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
global fun
def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


def creation_at(request):
    # if request.method == "POST":
    print(request.method)
    form: MO_form = MO_form(request.POST)
    print(form.errors)
    if form.is_valid():
        aa = form.cleaned_data['num_MO']
        print(" product_id:  ", aa)
        print('ok_ok_ok_ok_ok_ok_ok_ok_ok_ok_ok_ok_ok_ok_ok')
        form.save()
    return render(request, 'essai_mo.html', {'OFId': 1003211,'form': form})


def creation_dem(request):
    num_mo = "?"
    formmm: formm = formm(request.POST)
    if formmm.is_valid():
     ref = formmm.cleaned_data["project_Reference"]

     ref = str(ref)
     size = len(ref)
     ref = ref[:size - 1]
     ref = ref[16:len(ref)]
     print(ref)

     proj = project.objects.get(id_project=ref)
     print(proj.id_project)

     now = datetime.datetime.now()
     jours = now.strftime("%d")
     mois = now.strftime("%m")
     year = now.strftime("%Y")
     final = jours + mois + (year[2:4])
     print(final)
     num_mo = int_or_0(final)
     print(num_mo)
     list_OFf = MO.objects.filter(launch_Date=now.strftime("%Y-%m-%d"))
     index = len(list_OFf) + 1
     print(index)
     index = str(index)
     num_mo=str(num_mo)
     num_mo= num_mo + index
     num_mo = str(num_mo)
     print(num_mo)
     request.session['test'] = num_mo

     exemple = MO(project_Reference=proj, num_MO=num_mo, state_MO="waiting for validation", launch_Date=datetime.datetime.now().strftime("%Y-%m-%d"))
     exemple.save()

    form: AllForm = AllForm(request.POST)
    if form.is_valid():
        abc = form.cleaned_data["id_item"]
        request.session['username'] = abc
        #form.save()
        if request.session.has_key('username'):
         abc = request.session['username']

         if request.session.has_key('test') & request.session.has_key(''):
          acdb = request.session['test']
          MOO = MO.objects.get(num_MO=acdb)
          print(MOO.num_MO)
          objectt = piece.objects.get(id_item=abc, num_MO=None)
          print(objectt)
          #objectt.update(num_MO=MOO)
          objectt.num_MO = MOO
          objectt.save()
          print(objectt.num_MO)
     #if request.session.has_key(['test']):
      ##objectt.num_MO = request.session['test']
      #objectt.save()

    if request.session.has_key('test'):
     num = request.session['test']
     pieces = piece.objects.filter(num_MO=num)
    page = request.GET.get('page', 1)
    paginator = Paginator(pieces, 10)
    try:
        piece_list = paginator.page(page)
    except PageNotAnInteger:
        piece_list = paginator.page(1)
    except EmptyPage:
        piece_list = paginator.page(paginator.num_pages)
    return render(request, 'create_demand.html', {'formm': formmm, 'piece_list': piece_list, 'OFId': num_mo, 'form': form})


def creation_dem1(request):
    if request.method == "POST":
        qty = request.POST["quantity"]
        ref = request.POST["ref"]
        desig = request.POST["desig"]

        return render(request, 'create_demand.html', {'OFId': 1003211, 'qty': qty, 'ref': ref, 'desig': desig})

    else:
        return piece_detail(request)

def view_mo(request):
    a = MO.objects.all()
    b = filterr(request.GET, queryset=a)

    return render(request, 'Tasks.html', {'a': a, 'b': b})


def edit_dem(request):
    return render(request, 'edit_demand.html', {'OFId': 1003211})


def edit_prod(request):
    now = datetime.datetime.now()
    jours=now.strftime("%d")
    mois=now.strftime("%m")
    year=now.strftime("%Y")
    final = jours+mois+(year[2:4])
    print(final)
    num_mo = int_or_0(final)
    print(num_mo)
    list_OF = MO.objects.filter(launch_Date=now.strftime("%Y-%m-%d"))
    index = len(list_OF)
    print(index)
    indexx = int_or_0(index)
    num_mo = num_mo*10 + indexx + 1
    print(num_mo)
    return render(request, 'edit_resp_prod.html', {'OFId': 1003211})


def edit_at(request):
    return render(request, 'edit_at.html', {'OFId': 1003211})


def Tasks(request):
    a = MO.objects.all()
    b = filterr(request.GET, queryset=a)

    return render(request, 'Tasks.html', {'a': a, 'b': b})

def delete(request, id_auto):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    piece_example = piece.objects.filter(id_auto=id_auto)
    piece_example.delete()

    #return render(request, 'login.html')
    return redirect("/")

def update(request, id):
    mo = MO_form.objects.get(id=id)
    form = MO_form(request.POST, instance=mo)
    if form.is_valid():
        form.save()
        return redirect("/creation")
    return render(request, 'tesst.html', {'mo': mo})


def piece_detail(request):
    template_name = "create_demand.html"
    pieces = piece.objects.all()

    context = {'pieces': pieces}
    resp = render(request, template_name, context)
    return resp


def int_or_0(value):
    try:
        return int(value)
    except:
        return 0
