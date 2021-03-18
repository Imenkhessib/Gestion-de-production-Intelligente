from django.urls import path
from . import views
from . import manageOF

urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login, name='login')
]
