from django.shortcuts import render


def creation_prod(request):
    return render(request, 'create_resp_prod.html', {'OFId': 1003211})


def creation_at(request):
    return render(request, 'create_chef_at.html', {'OFId': 1003211})


def creation_dem(request):
    return render(request, 'create_demand.html', {'OFId': 1003211})


def creation_dem1(request):
    if request.method == "POST":
        qty = request.POST["quantity"]
        ref = request.POST["ref"]
        desig = request.POST["desig"]

        return render(request, 'create_demand.html', {'OFId': 1003211, 'qty': qty, 'ref': ref, 'desig': desig})

    else:
        return render(request, 'create_demand.html', {'OFId': 1003211})


def edit_dem(request):
    return render(request, 'edit_demand.html', {'OFId': 1003211})


def edit_prod(request):
    return render(request, 'edit_resp_prod.html', {'OFId': 1003211})


def edit_at(request):
    return render(request, 'edit_at.html', {'OFId': 1003211})
