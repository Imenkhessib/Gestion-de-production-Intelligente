from django.shortcuts import render, redirect
from .forms import AllForm, essai, item_form, formm, register
from .models import piece,MO, project
from .filters import filterr, filterrr
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
global fun
def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


def creation_at(request,num_MO):
    essai = 1
    essaii = 1
    essaiii = 1
    essai= request.POST["length"]
    essaii= request.get["width"]
    essaiii= request.get["thickness"]

    print(essai)
    print(essaii)
    print(essaiii)
    request.session['try1'] = essai
    request.session['try2'] = essaii
    request.session['try3'] = essaiii
    request.session['try4'] = num_MO
    items = piece.objects.filter(num_MO=num_MO)


    #form: item_form = item_form(request.POST)
    #item = piece.objects.get(id_auto={{keyy}})
    #form: AllForm = AllForm(request.POST, instance=item)
    #if form.is_valid():
    #essai = form.cleaned_data["length"]

    #print(essai)
    #essaii = form.cleaned_data["width"]
    #essaiii = form.cleaned_data["thickness"]


    return render(request, 'create_chef_at.html', {'OFId': num_MO, 'items': items, 'num_MO':num_MO, 'a':essai, 'b':essaii, 'c': essaiii})


def creation_dem(request):
    num_mo = "?"
    formmm: formm = formm(request.GET)
    print(formmm.errors)
    if formmm.is_valid():
     ref = formmm.cleaned_data["project_Reference"] # getting foreign-key value selected by user
###### extraction de la valeur de project_reference:
     ref = str(ref)
     size = len(ref)
     ref = ref[:size - 1]
     ref = ref[16:len(ref)]
     print(ref)
###### fin de l'extraction.
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
        abb = form.cleaned_data["id_item"]
        abcd = form.cleaned_data["designation"]
        abcde = form.cleaned_data["quantity"]
        abcdef = form.cleaned_data["CNC"]
        abcdefg = form.cleaned_data["Router"]
        abcdefgh = form.cleaned_data["laser_Cutters"]
        if request.session.has_key('test'):
            if 1:
                abc = request.session['test']
                abc = MO.objects.get(num_MO=abc)
                print(abc)

                objecttt = piece(num_MO=abc, id_item=abb, designation = abcd, quantity = abcde, CNC=abcdef, Router=abcdefg, laser_Cutters=abcdefgh, milling=abcdefgh)
                objecttt.save()
    pieces = piece.objects.filter(num_MO=9)
    if request.session.has_key('test'):
     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
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
    if request.session.has_key('test'):
        if 1:
            abc = request.session['test']
            print(abc)

    send_mail(
        "radhwen",
        "a new Manufacturing Order is made by Mr:" + request.user.username + ". please join the link to validate MO number:  " + abc + " \n 192.168.1.101:8000",
        "elhifradwen14@gmail.com",
        ['mohamedradhouan.elhif@isticbc.org'],
    )
    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

    return render(request, 'edit_demand.html', {'OFId': 1003211, 'abc': abc})


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
    return render(request, 'edit_dem.html', {'OFId': 1003211})


def Tasks(request):
    a = MO.objects.all()
    b = filterr(request.GET, queryset=a)

    return render(request, 'Tasks.html', {'a': a, 'b': b})

def update2(request, id_auto):
    #if request.session.has_key('try4'):
    #    id_auto = request.session['try4']
    print("success")
    piece_example = piece.objects.filter(id_auto=id_auto)
    if request.session.has_key('try1'):
     lengthh = request.session['try1']
     print(lengthh)
    if request.session.has_key('try2'):
     widthh = request.session['try2']
     print(widthh)
    if request.session.has_key('try3'):
     thicknesss = request.session['try3']
     print(thicknesss)
    piece_example = piece.objects.get(id_auto=id_auto)
    piece_example.length = lengthh
    piece_example.width = widthh
    piece_example.thickness = thicknesss

    piece_example.save()
    return redirect("/")
def delete(request, id_auto):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    piece_example = piece.objects.filter(pk=id_auto)
    piece_example.delete()
    #return render(request, 'login.html')
    return redirect("/creation")

def update(request, id_auto):
    item = piece.objects.get(pk=id_auto)
    data = {'id_item': '{{item.id_item}}'}
    form: AllForm = AllForm(request.POST, instance=item, initial=data)
    print(form.instance.id_auto)


    if form.is_valid():
        form.save()
        return redirect("/creation")
    return render(request, 'edit_dem.html', {'item': item, 'form': form})


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
def loginn(request):
    logout(request)
    username = request.POST.get("exampleInputEmail")
    password = request.POST.get("exampleInputPassword")
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        request.session["user_name"] = username
        print("successssssss")
        login(request, user)
        return redirect("/")
    print("failed")
    return render(request, 'login.html', {'username': username})

