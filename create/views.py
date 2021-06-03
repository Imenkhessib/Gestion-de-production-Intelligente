from lib2to3.fixes.fix_input import context
from django.http import HttpResponseRedirect
import os
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AllForm, essai, item_form, formm, register, Foorm, mo_cause, form_piece
from .models import piece, MO, project, task, p_task
from .filters import filterr, filterrrr
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from simple_history.models import pre_create_historical_record
global fun


def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


@login_required(login_url='login')
def creation_at(request, num_MO):
    items = piece.objects.filter(num_MO=num_MO)
    a = request.POST.get("a")  # length
    b = request.POST.get("b")  # width
    c = request.POST.get("c")  # thickness
    d = request.POST.get("d")  # id_auto (hidden field)
    e = request.POST.get("e")  # material
    f = request.POST.get("f")  # scheduled_hours_CNC
    g = request.POST.get("g")  # scheduled_hours_laser_cutters
    h = request.POST.get("h")  # scheduled_hours_Router
    i = request.POST.get("i")  # scheduled_hours_milling
    if d != None:
        item = piece.objects.get(id_auto=d)
        item.length = a
        item.width = b
        item.thickness = c
        item.material = e
        item.scheduled_hours_CNC = f
        print(f)
        item.scheduled_hours_laser_cutters = g
        print(g)
        item.scheduled_hours_Router = h
        print(h)
        item.scheduled_hours_Milling = i
        item.save()
        redirect("creation/atelier/num_mo")
    page = request.GET.get('page', 1)
    paginator = Paginator(items, 6)
    try:
        piece_list = paginator.page(page)
    except PageNotAnInteger:
        piece_list = paginator.page(1)
    except EmptyPage:
        piece_list = paginator.page(paginator.num_pages)
    #     Générer les taches à partir des pièces + qualif
    if request.POST.get("tasks"):
            A = task.objects.filter(num_mo=num_MO)
            A.delete()
            mo = MO.objects.get(num_MO=num_MO)
            index = 0
            for i in piece_list:
                if "cnc" in i.machines:
                    pt = p_task()
                    pt.MO = mo
                    pt.item = i
                    pt.qualification = "cnc"
                    pt.scheduled_hours = i.scheduled_hours_CNC
                    pt.qte = i.quantity
                    pt.save()
                    for j in range(0, i.quantity):
                     index += 1
                     task1 = task()
                     task1.qualification = "cnc"
                     task1.duration = i.scheduled_hours_CNC / i.quantity
                     task1.duration *= 60
                     task1.state_task = "to do"
                     task1.num_item = i
                     task1.id_task = index
                     task1.num_mo = mo
                     task1.p_task = pt
                     task1.save()
                index = 0
                if "router" in i.machines:
                    pt = p_task()
                    pt.MO = mo
                    pt.item = i
                    pt.qualification = "cnc"
                    pt.scheduled_hours = i.scheduled_hours_Router
                    pt.qte = i.quantity
                    pt.save()

                    for j in range(0, i.quantity):
                     index += 1
                     task1 = task()
                     task1.qualification = "Router"
                     task1.duration = i.scheduled_hours_Router / i.quantity
                     task1.duration *= 60
                     task1.state_task = "to do"
                     task1.id_task = index
                     task1.num_item = i
                     task1.num_mo = mo
                     task1.p_task = pt
                     task1.save()
                index = 0
                if "milling" in i.machines:
                    pt = p_task()
                    pt.MO = mo
                    pt.item = i
                    pt.qualification = "milling"
                    pt.scheduled_hours = i.scheduled_hours_Milling
                    pt.qte = i.quantity
                    pt.save()

                    for j in range(0, i.quantity):
                     index += 1
                     task1 = task()
                     task1.qualification = "milling"
                     task1.duration = i.scheduled_hours_Milling / i.quantity
                     task1.duration *= 60
                     task1.id_task = index
                     task1.state_task = "to do"
                     task1.num_mo = mo
                     task1.num_item = i
                     task1.p_task = pt
                     task1.save()
                index = 0
                if "lathe" in i.machines:
                    pt = p_task()
                    pt.MO = mo
                    pt.item = i
                    pt.qualification = "lathe"
                    pt.scheduled_hours = i.scheduled_hours_lathe
                    pt.qte = i.quantity
                    pt.save()
                    for j in range(0, i.quantity):
                     index += 1
                     task1 = task()
                     task1.qualification = "lathe"
                     task1.duration = i.scheduled_hours_lathe / i.quantity
                     task1.duration *= 60
                     task1.id_task = index
                     task1.state_task = "to do"
                     task1.num_item = i
                     task1.num_mo = mo
                     task1.p_task = pt
                     task1.save()
                     index = 0
                if "laser_cutter" in i.machines:
                    pt = p_task()
                    pt.MO = mo
                    pt.item = i
                    pt.qualification = "laser_cutter"
                    pt.scheduled_hours = i.scheduled_hours_laser_cutters
                    pt.qte = i.quantity
                    pt.save()

                    for j in range(0, i.quantity):
                     index += 1
                     task1 = task()
                     task1.qualification = "laser_cutter"
                     task1.duration = i.scheduled_hours_laser_cutters / i.quantity
                     task1.duration *= 60
                     task1.state_task = "to do"
                     task1.id_task = index
                     task1.num_item = i
                     task1.num_mo = mo
                     task1.p_task = pt
                     task1.save()
                     index = 0
    return render(request, 'create_chef_at.html', {'OFId': num_MO, 'items': items, "piece_list": piece_list})

@login_required(login_url='login')
def calcul(request):
    pt = p_task.objects.all()
    for i in pt:
        c = 0
        t = task.objects.filter(p_task=i)
        for j in t:
            if j.progress_percentage == 100.0:
                c += 1
        i.performed_hours = (i.scheduled_hours / i.qte) * c
        i.remaining_hours = i.scheduled_hours - i.performed_hours
        i.percentage_progression = (i.performed_hours / i.scheduled_hours) * 100
        i.save()
    return render(request, "calcul.html", {"pt": pt})

@login_required(login_url='login')
def creation_dem(request):
    ref = "0"
    if request.session.has_key('proj'):
        ref = request.session['proj']
    num_mo = "0"
    if request.session.has_key('test'):
        num_mo = request.session['test']

    formmm: formm = formm(request.POST)
    if formmm.is_valid():
        for i in range(1, 10000):
            if len(MO.objects.filter(num_MO=i)) == 0:
                j = str(i)
                num_mo = j
                print(num_mo)

                break

        ref = formmm.cleaned_data["project_Reference"]

        ref = str(ref)
        size = len(ref)
        ref = ref[:size - 1]
        ref = ref[16:len(ref)]
        print(ref)

        proj = project.objects.get(project_Reference=ref)
        print(proj.project_Reference)
        request.session['proj'] = ref

        request.session['test'] = num_mo

        exemple = MO(project_Reference=proj, num_MO=num_mo, state_MO="waiting for validation",
                     launch_Date=datetime.datetime.now().strftime("%Y-%m-%d"))
        exemple.save()

    # ***************************************************************
    form: AllForm = AllForm(request.POST, request.FILES)
    if form.is_valid():
        abb = form.cleaned_data["id_item"]
        print(abb)
        abcd = form.cleaned_data["designation"]
        abcde = form.cleaned_data["quantity"]
        abcdef = form.cleaned_data["CNC"]
        print(abcdef)
        abcdefg = form.cleaned_data["Router"]
        abcdefgh = form.cleaned_data["laser_Cutters"]
        machines = form.cleaned_data["machines"]
        two_d = form.cleaned_data["two_d"]
        print(two_d)
        three_d = form.cleaned_data["three_d"]
        abcdefgg = form.cleaned_data["milling"]
        testt = form.cleaned_data["Test"]
        if request.session.has_key('test'):
            if 1:
                abc = request.session['test']
                abc = MO.objects.get(num_MO=abc)
                print(abc)

                objecttt = piece(num_MO=abc, id_item=abb, designation=abcd, quantity=abcde, CNC=testt,
                                 machines=machines, Router=abcdefg, laser_Cutters=abcdefgh, milling=abcdefgg,
                                 two_d=two_d, three_d=three_d)
                objecttt.save()
                form = AllForm()
    else:
        messages.error(request, "not checked")
        print("successssssssssssssssssssssssssssss")
    pieces = piece.objects.filter(num_MO=9)
    if request.session.has_key('test'):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        num = request.session['test']
        if request.POST.get("clear"):
            projj = project.objects.get(project_Reference=ref)

            subject = 'MO Confirmation'
            from_email = 'pferadh2021@gmail.com'
            to_emails = projj.project_chief.email, request.user.email

            newnew = MO.objects.get(num_MO=num_mo)
            newnew.mechanical_engineer = request.user
            newnew.date_val_dem = str(datetime.date.today())
            newnew.save()

            context = {
                'num_mo': num_mo,
                'a': request.user
            }
            msg_html = render_to_string('email_valid.html', context)

            msg = EmailMultiAlternatives(subject, msg_html, from_email, bcc=to_emails)
            msg.attach_alternative(msg_html, "text/html")
            msg.send()

            ref = "0"
            num = "0"
            request.session['test'] = num
            request.session['proj'] = ref
        if request.POST.get("cancel"):
            ref = "0"
            num = "0"
            request.session['test'] = num
            request.session['proj'] = ref
        pieces = piece.objects.filter(num_MO=num)
    page = request.GET.get('page', 1)
    paginator = Paginator(pieces, 10)
    try:
        piece_list = paginator.page(page)
    except PageNotAnInteger:
        piece_list = paginator.page(1)
    except EmptyPage:
        piece_list = paginator.page(paginator.num_pages)

    return render(request, 'create_demand.html', {'formm': formmm, 'piece_list': piece_list, 'OFId': num_mo, 'form': form, 'proj': ref})


@login_required(login_url='login')
def creation_dem1(request):
    if request.method == "POST":
        qty = request.POST["quantity"]
        ref = request.POST["ref"]
        desig = request.POST["desig"]

        return render(request, 'create_demand.html', {'OFId': 1003211, 'qty': qty, 'ref': ref, 'desig': desig})

    else:
        return piece_detail(request)


@login_required(login_url='login')
def view_mo(request):
    a = MO.objects.all()
    b = filterr(request.GET, queryset=a)

    return render(request, 'display_mo.html', {'a': a, 'b': b})


@login_required(login_url='login')
def edit_dem(request):
    if request.session.has_key('test'):
        if 1:
            abc = request.session['test']
            print(abc)

    send_mail(
        "radhwen",
        "a new Manufacturing Order is made by Mr:" + request.user.username + ". please join the link to validate MO number:  " + abc + " \n http://127.0.0.1:8000",
        "elhifradwen14@gmail.com",
        ['mohamedradhouan.elhif@isticbc.org'],
    )
    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

    return render(request, 'edit_demand.html', {'OFId': 1003211, 'abc': abc})


@login_required(login_url='login')
def edit_prod(request):
    now = datetime.datetime.now()
    jours = now.strftime("%d")
    mois = now.strftime("%m")
    year = now.strftime("%Y")
    final = jours + mois + (year[2:4])
    print(final)
    num_mo = int_or_0(final)
    print(num_mo)
    list_OF = MO.objects.filter(launch_Date=now.strftime("%Y-%m-%d"))
    index = len(list_OF)
    print(index)
    indexx = int_or_0(index)
    num_mo = num_mo * 10 + indexx + 1
    print(num_mo)
    return render(request, 'edit_resp_prod.html', {'OFId': 1003211})


def edit_at(request):
    return render(request, 'edit_dem.html', {'OFId': 1003211})


def Tasks(request):
    list = task.objects.all()
    return render(request, 'task_history.html', {'tasks': list})


@login_required(login_url='login')
def delete(request, id_auto):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    piece_example = piece.objects.filter(pk=id_auto)
    piece_example.delete()

    # return render(request, 'login.html')
    return redirect("/creation")

@login_required(login_url='login')
def affecter_tache(request, id):
    task_example = task.objects.get(pk=id)
    task_example.start_datetime = datetime.datetime.now()
    task_example.id_user = request.user
    task_example.state_task = "In Progress"
    task_example.save()

    # return render(request, 'login.html')
    return redirect("/creation/Tasks")

@login_required(login_url='login')
def tache_accomplie(request, id):
    task_example = task.objects.get(pk=id)
    task_example.finish_stop_datetime = datetime.datetime.now()
    task_example.state_task = "Done"
    task_example.progress_percentage = 100.0
    task_example.save()

    return redirect("/creation/Tasks")


@login_required(login_url='login')
def emettre_tache(request, id):
    task_example = task.objects.get(pk=id)
    task_example.finish_stop_datetime = datetime.datetime.now()
    task_example.state_task = "On Hold"
    d = str(task_example.finish_stop_datetime)
    d = d[:21]
    print(d)
    dd = str(task_example.start_datetime)
    dd = dd[:21]
    print(dd)
    d1 = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
    print(d1)
    d2 = datetime.datetime.strptime(dd, '%Y-%m-%d %H:%M:%S.%f')
    print(d2)
    print(d1 - d2)
    ddd = d1 - d2
    ddd = str(ddd)
    hours = ddd[:1]
    hours = int(hours)
    print(hours)
    minutes = ddd[2 : 4]
    minutes = int(minutes)
    print(minutes)
    seconds = ddd[5:7]
    seconds = int(seconds)
    print(seconds)
    total_min = hours * 60 + minutes + seconds/60
    print(total_min)
    task_example.real_duration += total_min
    task_example.progress_percentage = (task_example.real_duration / task_example.duration)*100

    task_example.save()

    # return render(request, 'login.html')
    return redirect("/creation/Tasks")


@login_required(login_url='login')
def update(request, id_auto):
    item = piece.objects.get(pk=id_auto)
    i = get_object_or_404(piece, pk=id_auto)
    initial_dict = {
        "id_item": item.id_item,
        "designation": item.designation,
        "two_d": item.two_d,
        "three_d": item.three_d,
    }
    form: Foorm = Foorm(request.POST or None, request.FILES or None, instance=i, initial=initial_dict)
    if form.is_valid():
        a = form.cleaned_data["two_d"]
        print(a)
        i = form.save(commit=False)
        i.save()
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


@login_required(login_url='login')
def create_dem_validate(request, num_mo):
    OF = MO.objects.get(num_MO=num_mo)
    form: AllForm = AllForm(request.POST, request.FILES)
    if form.is_valid():
        abb = form.cleaned_data["id_item"]
        print(abb)
        abcd = form.cleaned_data["designation"]
        abcde = form.cleaned_data["quantity"]
        abcdef = form.cleaned_data["CNC"]
        print(abcdef)
        abcdefg = form.cleaned_data["Router"]
        abcdefgh = form.cleaned_data["laser_Cutters"]
        machines = form.cleaned_data["machines"]
        two_d = form.cleaned_data["two_d"]
        print(two_d)
        three_d = form.cleaned_data["three_d"]
        abcdefgg = form.cleaned_data["milling"]
        if 1:
            if 1:
                print("it was the problem")
                abc = MO.objects.get(num_MO=num_mo)
                print(abc)

                objecttt = piece(num_MO=abc, id_item=abb, designation=abcd, quantity=abcde, machines=machines,
                                 two_d=two_d, three_d=three_d)
                objecttt.save()
                print("aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccc")
                form = AllForm()
    else:
        messages.error(request, "not checked")
        print("successssssssssssssssssssssssssssss")
    pieces = piece.objects.filter(num_MO=9)
    if request.session.has_key('test'):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        num = request.session['test']
        if request.POST.get("clear"):
            ref = OF.project_Reference
            projj = project.objects.get(project_Reference=ref)

            subject = 'MO Confirmation'
            from_email = 'pferadh2021@gmail.com'
            to_emails = projj.project_chief.email, request.user.email

            newnew = MO.objects.get(num_MO=num_mo)
            newnew.mechanical_engineer = request.user
            newnew.date_val_dem = str(datetime.date.today())
            newnew.save()

            context = {
                'num_mo': num_mo,
                'a': request.user
            }
            msg_html = render_to_string('email_valid.html', context)

            msg = EmailMultiAlternatives(subject, msg_html, from_email, bcc=to_emails)
            msg.attach_alternative(msg_html, "text/html")
            msg.send()

    pieces = piece.objects.filter(num_MO=num_mo)
    page = request.GET.get('page', 1)
    paginator = Paginator(pieces, 10)
    try:
        piece_list = paginator.page(page)
    except PageNotAnInteger:
        piece_list = paginator.page(1)
    except EmptyPage:
        piece_list = paginator.page(paginator.num_pages)

    return render(request, 'create_dem_validate.html',
                  {'piece_list': piece_list, 'OFId': num_mo, 'form': form})


@login_required(login_url='login')
def edit_item(request, id_auto):
    item = piece.objects.get(pk=id_auto)
    i = get_object_or_404(piece, pk=id_auto)
    num_mo = i.num_MO
    ref = str(num_mo)
    size = len(ref)
    ref = ref[:size - 1]
    ref = ref[11:len(ref)]
    print(ref)
    initial_dict = {
        "id_item": item.id_item,
        "designation": item.designation,
        "two_d": item.two_d,
        "three_d": item.three_d,
    }
    form: Foorm = Foorm(request.POST or None, request.FILES or None, instance=i, initial=initial_dict)
    if form.is_valid():
        a = form.cleaned_data["two_d"]
        print(a)
        i = form.save(commit=False)
        i.save()
        return redirect("http://127.0.0.1:8000/creation/updatee/" + ref)
    return render(request, 'edit_dem_validate.html', {'item': item, 'form': form})



@login_required(login_url='login')
def edit1_item(request, id_auto):
    a = str(id_auto)
    item = piece.objects.get(pk=id_auto)
    i = get_object_or_404(piece, pk=id_auto)
    num_mo = i.num_MO
    ref = str(num_mo)
    size = len(ref)
    ref = ref[:size - 1]
    ref = ref[11:len(ref)]
    print(ref)

    initial_dict = {
        "material": item.material,
        "length": item.length,
        "width": item.width,
        "thickness": item.thickness,
        "scheduled_hours_CNC": item.scheduled_hours_CNC,
        "scheduled_hours_Milling": item.scheduled_hours_Milling,
        "scheduled_hours_Router": item.scheduled_hours_Router,
        "scheduled_hours_cutters": item.scheduled_hours_laser_cutters,
    }
    form: form_piece = form_piece(request.POST or None, instance=i, initial=initial_dict)
    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        return redirect("http://127.0.0.1:8000/creation/atelier/" + ref)
    print(form.errors)


    return render(request, "edit_items.html",{"form": form, "item": item})

@login_required(login_url='login')
def validation(request, num_mo):

    var = MO.objects.get(num_MO=num_mo)
    demandeur = User.objects.get(id=var.mechanical_engineer.id)
    proj_ref = var.project_Reference
    print(proj_ref)
    i = get_object_or_404(MO, pk=num_mo)
    ref = str(proj_ref)
    size = len(ref)
    ref = ref[:size - 1]
    ref = ref[16:len(ref)]
    var1 = project.objects.get(project_Reference=ref)
    proj_manager = User.objects.get(id=var1.project_chief.id)
    validation = User.objects.get(id=3)
    prod = User.objects.get(id=5)
    atelier = User.objects.get(id=6)

    print(var1)
    mo_form: mo_cause = mo_cause(request.POST, instance=i)

    if mo_form.is_valid():
        print("pppppppppp")
        cause = mo_form.cleaned_data["cause_invalid"]
        print("pooooooooooop")
        i.cause_invalid = cause
        i.save()
        subject = 'MO invalidation'
        from_email = 'pferadh2021@gmail.com'
        to = demandeur.email

        context = {
            'cause': cause,
            'num_mo': num_mo,
            'a': request.user,
            'dem': demandeur,
        }
        msg_html = render_to_string('email.html', context)
        msg = EmailMultiAlternatives(subject, msg_html, from_email, [to])
        msg.attach_alternative(msg_html, "text/html")
        msg.send()

        subject = 'MO invalidation'
        from_email = 'pferadh2021@gmail.com'
        to = request.user.email
        context = {
            'cause': cause,
            'num_mo': num_mo,
            'a': request.user,
            'dem': demandeur,
        }
        msg_html = render_to_string('email_inv.html', context)
        msg = EmailMultiAlternatives(subject, msg_html, from_email, [to])
        msg.attach_alternative(msg_html, "text/html")
        msg.send()
    else:
        print(mo_form.errors)

    if request.POST.get("validate_proj"):
        subject = 'MO Confirmation'
        from_email = 'pferadh2021@gmail.com'
        to_emails = prod.email, request.user.email
        context = {
            'num_mo': num_mo,
            'a': request.user
        }
        msg_html = render_to_string('email_valid.html', context)

        msg = EmailMultiAlternatives(subject, msg_html, from_email, bcc=to_emails)
        msg.attach_alternative(msg_html, "text/html")
        msg.send()

        var.date_val_chefproj = datetime.date.today()
        var.save()

    if request.POST.get("val_eng"):
        subject = 'MO Confirmation'
        from_email = 'pferadh2021@gmail.com'
        to_emails = prod.email, request.user.email
        context = {
            'num_mo': num_mo,
            'a': request.user
        }
        msg_html = render_to_string('email_valid.html', context)

        msg = EmailMultiAlternatives(subject, msg_html, from_email, bcc=to_emails)
        msg.attach_alternative(msg_html, "text/html")
        msg.send()

        var.date_val_respval = datetime.date.today()
        var.save()

    if request.POST.get("val_prod"):
        subject = 'MO Confirmation'
        from_email = 'pferadh2021@gmail.com'
        to_emails = atelier.email, request.user.email
        context = {
            'num_mo': num_mo,
            'a': request.user
        }
        msg_html = render_to_string('email_valid.html', context)

        msg = EmailMultiAlternatives(subject, msg_html, from_email, bcc=to_emails)
        msg.attach_alternative(msg_html, "text/html")
        msg.send()

        var.date_val_respprod = datetime.date.today()
        var.save()

    if request.POST.get("val_at"):
        subject = 'MO Confirmation'
        from_email = 'pferadh2021@gmail.com'
        to = request.user.email
        context = {
            'num_mo': num_mo,
            'a': request.user
        }
        msg_html = render_to_string('email_valid.html', context)

        msg = EmailMultiAlternatives(subject, msg_html, from_email, [to])
        msg.attach_alternative(msg_html, "text/html")
        msg.send()

        var.date_val_chefat = datetime.date.today()
        var.save()


        # génération d'un nouveau OF identique à celui au cours de validation
        new = MO.objects.get(num_MO=num_mo)
        now = datetime.datetime.now()
        new.launch_Date=now.strftime("%Y-%m-%d")
        new.save()
        # génération d'un nouveau numero
        jours = now.strftime("%d")
        mois = now.strftime("%m")
        year = now.strftime("%Y")
        final = jours + mois + (year[2:4])
        num = int_or_0(final)
        list_OFf = MO.objects.filter(launch_Date=now.strftime("%Y-%m-%d"))
        index = len(list_OFf)
        index = str(index)
        num=str(num)
        num = num + index
        num = str(num)
#####################################################################################################
        # établir une relation entre les pieces et le nouveau Ordre de fabrication
        trash = MO.objects.get(num_MO=num_mo)
        testtt = trash
        testtt.num_MO = num
        testtt.state_MO = "released"
        testtt.launch_Date = now.strftime("%Y-%m-%d")
        testtt.save()

        pieces_list = piece.objects.filter(num_MO=num_mo)
        print(len(pieces_list))
        for nnnnnnnn in pieces_list:
            nnnnnnnn.num_MO = testtt
            print(nnnnnnnn.id_auto)
            nnnnnnnn.save()

        # suppression de l'ancien objet MO
        egg = MO.objects.get(num_MO=num_mo)
        print(egg)
        egg.delete()


    return render(request, 'validation_cycle.html',
                  {'OFId': num_mo, 'proj': ref, 'mo_form': mo_form, 'proj_manager': proj_manager,
                   'demandeur': demandeur, 'var': var})


@login_required(login_url='login')
def Machines(request):
    return render(request, 'Machines.html')


@login_required(login_url='login')
def print_mo(request, num_mo):
    list = piece.objects.filter(num_MO=num_mo)
    mo = MO.objects.get(num_MO=num_mo)
    ref = mo.project_Reference
    ref = str(ref)
    size = len(ref)
    ref = ref[:size - 1]
    ref = ref[16:len(ref)]
    print(ref)
    proj = project.objects.get(project_Reference=ref)
    name = proj.name_project
    lenn = len(list)
    nb_pages = lenn // 15
    if lenn % 15 != 0:
        nb_pages = nb_pages + 1
    lisst = []
    for i in range(0, nb_pages):
        lisst.append(i)
    print(len(lisst))
    date = datetime.date.today().strftime('%d/%m/%Y')
    return render(request, "print.html",
                  {"list": list, "OFId": num_mo, "ref": ref, "lisst": lisst, "nb_pages": nb_pages, 'date': date,
                   'name': name})

def changes_history(request):
    histories = MO.history.all()
    b = filterrrr(request.GET, queryset=histories)
    for i in histories:
     print(i.history_id, ": ", i.history_type)

    return render(request, "changes_history.html", {"list": histories, 'b':b})

def tasks(request):
    A = task.objects.all()
    passs = os.environ.get('mail_pass')
    print(passs)
    return render(request, "tasks.html", {"A":A})