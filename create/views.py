from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import request,HttpResponse


def creation_prod(request):
    return render(request,'create_resp_prod.html', {'OFId':1003211})
def creation_at(request):
        return render(request,'create_chef_at.html',  {'OFId':1003211} )

def creation_dem(request):
    b=0
    return render(request, 'create_demand.html', {'OFId': 1003211,'bas':b})

def creation_dem1(request):
        if request.method == "POST":
            aa = request.POST["quantity"]
            bb = request.POST["ref"]
            cc = request.POST["desig"]
            nums=[1,2,3]
            return render(request, 'create_demand.html', {'OFId': 1003211, 'bas': aa,'bb':bb, 'cc':cc})

        else:
            return render(request, 'create_demand.html', {'OFId': 1003211})



def edit_dem(request):
    return render(request,'edit_demand.html' ,  {'OFId':1003211})
def edit_prod(request):
    return render(request,'edit_resp_prod.html' ,  {'OFId':1003211})
def edit_at(request):
    return render(request,'edit_at.html' ,  {'OFId':1003211})