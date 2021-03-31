from django.urls import path
from . import views

urlpatterns = [
    path('production', views.creation_prod, name='create_prod'),
    path('atelier',views.creation_at, name='create_at'),
    path('',views.creation_dem, name='create_dem'),
    path('test',views.creation_dem, name='create_dem'),
    path('edit_dem',views.edit_dem, name='edit_dem'),
    path('edit_prod',views.edit_prod, name='edit_prod'),
    path('edit_at',views.edit_at, name='edit_at'),
    path('Tasks',views.Tasks, name='Tasks')
]
