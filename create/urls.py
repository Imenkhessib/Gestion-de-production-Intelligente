from django.urls import path
from . import views

urlpatterns = [
    path('production', views.creation_prod, name='create_prod'),
    path('atelier', views.creation_at, name='create_at'),
    path('', views.creation_dem, name='create_dem'),
    path('test', views.creation_dem, name='create_dem'),
    path('view_mo', views.view_mo, name='view_mo'),
    path('Tasks', views.Tasks, name='Tasks'),
    path('validation', views.Validation, name='validation'),
path('Machines', views.Machines, name='Machines'),
]
