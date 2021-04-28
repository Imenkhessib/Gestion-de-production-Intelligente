from django import forms
from .models import piece, MO, project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

machine_choices = (
    ('cnc', 'cnc'),
    ('router', 'router'),
    ('milling', 'milling'),
    ('lathe', 'lathe'),
    ('laser_cutter', 'laser_cutter'),
)


class AllForm(forms.ModelForm):
    Test = forms.BooleanField(required=False, initial=False)

    # file = forms.FileField()
    class Meta:
        model = piece
        fields = (
            'id_item', 'designation', 'quantity', 'CNC', 'Router', 'laser_Cutters', 'milling', 'machines', 'two_d',
            'three_d')
        widgets = {
            'id_item': forms.TextInput(
                attrs={'id': 'id_item', 'class': "form-control form-control-user", 'type': "text"}),
            'designation': forms.TextInput(
                attrs={'id': 'desig', 'class': "form-control form-control-user", 'type': "text"}),
            'quantity': forms.NumberInput(
                attrs={'id': 'quantity', 'class': "form-control form-control-user", 'type': "number"}),
            'machines': forms.CheckboxSelectMultiple(
                attrs={'id': 'machinery', 'required': 'True', 'class': 'machine_choices'}
            ),
            'three_d': forms.FileInput(
                attrs={'class': 'plan3d'}),
            'two_d': forms.FileInput(
                attrs={'class': 'plan2d', 'required': 'True'}),

        }


class Foorm(forms.ModelForm):
    Test = forms.BooleanField(required=False, initial=False)

    # file = forms.FileField()
    class Meta:
        model = piece
        fields = (
            'id_item', 'designation', 'quantity', 'CNC', 'Router', 'laser_Cutters', 'milling', 'machines', 'two_d',
            'three_d')
        widgets = {
            'id_item': forms.TextInput(
                attrs={'id': 'id_item', 'class': "form-control form-control-user", 'type': "text"}),
            'designation': forms.TextInput(
                attrs={'id': 'desig', 'class': "form-control form-control-user", 'type': "text"}),
            'quantity': forms.NumberInput(
                attrs={'id': 'quantity', 'class': "form-control form-control-user", 'type': "number"}),
            'machines': forms.CheckboxSelectMultiple(
                attrs={'id': 'machinery', 'class': 'machine_choices'}
            ),
            'three_d': forms.FileInput(
                attrs={'class': 'plan3d'}),
            'two_d': forms.FileInput(
                attrs={'class': 'plan2d'}),

        }


class essai(forms.ModelForm):
    class Meta:
        model = project
        fields = ('project_Reference', 'name_project', 'client', 'project_chief')


class item_form(forms.ModelForm):
    class Meta:
        model = piece
        fields = "__all__"


class formm(forms.ModelForm):
    class Meta:
        model = MO
        # fields = ('id_project',)
        fields = ('project_Reference',)
        widgets = {
            'project_Reference': forms.Select(
                attrs={'id': '', 'class': "form-control form-control-user", 'type': "text", 'value': 'item.id_auto'})
        }
        # project_Ref = forms.CharField()


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
