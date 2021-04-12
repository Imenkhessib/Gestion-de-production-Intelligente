from django import forms
from .models import piece,MO,project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AllForm(forms.ModelForm):
 #file = forms.FileField()
 class Meta:
   model = piece
   fields = ( 'id_item', 'designation', 'quantity', 'CNC', 'Router', 'laser_Cutters', 'milling')
   widgets = {
       #'num_MO': forms.TextInput(attrs={'id': 'desig', 'class': "form-control form-control-user", 'type': "text"}),
       'id_item': forms.TextInput(attrs={'id': '', 'class': "form-control form-control-user", 'type': "text", 'value': 'item.id_auto'}),
       'designation': forms.TextInput(attrs={'id': 'desig', 'class': "form-control form-control-user", 'type': "text"}),
       'quantity': forms.NumberInput(attrs={'id': 'quantity', 'class': "form-control form-control-user", 'type': "number"}),
       'CNC': forms.CheckboxInput(attrs={'id': 'quantity', 'class': "form-control form-control-user"}),
       'Router': forms.CheckboxInput(attrs={'id': 'quantity', 'class': "form-control form-control-user"}),
       'laser_Cutters': forms.CheckboxInput(attrs={'id': 'quantity', 'class': "form-control form-control-user"}),
       'milling': forms.CheckboxInput(attrs={'id': 'quantity', 'class': "form-control form-control-user"}),
   }

class essai(forms.ModelForm):
    class Meta:
        model = project
        fields = ('id_project', 'name_project', 'client', 'num_bon_commande', 'project_chief')

class item_form(forms.ModelForm):
    class Meta:
        model = piece
        fields = "__all__"

class formm(forms.ModelForm):
    class Meta:
     model = MO
     #fields = ('id_project',)
     fields = ('project_Reference',)
     #project_Ref = forms.CharField()


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

