from django.urls import path
from . import views

urlpatterns = [
    path('production', views.creation_prod, name='create_prod'),
    path('atelier/<int:num_MO>', views.creation_at, name='create_at'),
    path('', views.creation_dem, name='create_dem'),
    path('test', views.creation_dem, name='create_dem'),
    path('edit_dem', views.edit_dem, name='edit_dem'),
    path('edit_prod', views.edit_prod, name='edit_prod'),
    path('edit_at', views.edit_at, name='edit_at'),
    path('Tasks', views.Tasks, name='Tasks'),
    path('delete/<int:id_auto>', views.delete, name='delete'),
    path('update/<int:id_auto>', views.update, name='update'),
    path('view_mo', views.view_mo, name='view_mo'),
    path('loginn', views.loginn, name='login'),
    path('validation/<int:num_mo>', views.validation, name='validation'),
    path('Machines', views.Machines, name='Machines'),
    path('atelier', views.creation_at, name='atelier'),
    path('validation/<int:num_mo>', views.validation, name='email'),
    path('validation/<int:num_mo>', views.creation_dem, name='email_valid'),
    path('print/<int:num_mo>', views.print_mo, name='print'),
    path('updatee/<int:num_mo>', views.create_dem_validate),
    path('updateee/<int:id_auto>', views.edit_item),
    path('update1/<int:id_auto>', views.edit1_item),
    path('history1', views.changes_history, name='history'),
]
