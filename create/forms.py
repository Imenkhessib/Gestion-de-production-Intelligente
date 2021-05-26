from django import forms
from .models import piece, MO, project, access_control
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


class access_control(forms.ModelForm):
    class Meta:
        model = access_control
        fields = 'permission_class', 'id_user',
        widgets = {
            'permission_class': forms.NumberInput(
                attrs={'id': 'perm_class', 'class': "form-control form-control-user", 'type': "number", 'min': '0',
                       'max': '3'}),
            'id_user': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
        }

class mo_edit(forms.ModelForm):
    class Meta:
        model = MO
        fields = 'priority_MO', 'state_MO', 'date_dem_prev', 'date_dem_real', 'date_cloture_prev', 'date_cloture_act', 'date_cloture_real',
        widgets = {
            'priority_MO': forms.NumberInput(
                attrs={'id': 'perm_class', 'class': "form-control form-control-user", 'type': "number", 'min': 0}),
            'state_MO': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
            'date_dem_prev': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
            'date_dem_real': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
            'date_cloture_prev': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
            'date_cloture_act': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
            'date_cloture_real': forms.NumberInput(attrs={'id': 'id_user', 'class': "form-control form-control-user"}),
        }


class mo_cause(forms.ModelForm):
    class Meta:
        model = MO
        fields = 'cause_invalid',
        widgets = {
            'cause_invalid': forms.Textarea(
                attrs={'required': 'True', 'label': 'Precise the cause of invalidation',
                       'rows': '4',
                       'cols': '60',
                       'maxlength': '200',
                       'class': "form-control form-control-user"}
            )
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


class form_piece(forms.ModelForm):
    class Meta:
        model = piece
        fields = ('material', 'length', 'width', 'thickness', "scheduled_hours_CNC", "scheduled_hours_Milling",
                  "scheduled_hours_Router", "scheduled_hours_laser_cutters", "scheduled_hours_Lathe")
        widgets = {
            'material': forms.TextInput(
                attrs={'id': 'material', 'class': "form-control form-control-user", 'type': "text"}),
            'length': forms.NumberInput(
                attrs={'id': 'length', 'required': 'True', 'class': "form-control form-control-user"}),
            'width': forms.NumberInput(
                attrs={'id': 'width', 'required': 'True', 'class': "form-control form-control-user"}),
            'thickness': forms.NumberInput(
                attrs={'id': 'thick', 'required': 'True', 'class': 'form-control form-control-user'}),
            'scheduled_hours_CNC': forms.NumberInput(
                attrs={'id': 'cnc_h', 'required': 'True', 'class': 'form-control form-control-user'}),
            'scheduled_hours_Milling': forms.NumberInput(
                attrs={'id': 'milling_h', 'required': 'True', 'class': 'form-control form-control-user'}),
            'scheduled_hours_Router': forms.NumberInput(
                attrs={'id': 'router_h', 'required': 'True', 'class': 'form-control form-control-user'}),
            'scheduled_hours_laser_cutters': forms.NumberInput(
                attrs={'id': 'laser_h', 'required': 'True', 'class': 'form-control form-control-user'}
            ),
            'scheduled_hours_Lathe': forms.NumberInput(
                attrs={'id': 'lathe_h', 'required': 'True', 'class': 'form-control form-control-user'}
            ),

        }


class essai(forms.ModelForm):
    class Meta:
        model = project
        fields = ('project_Reference', 'name_project', 'client')


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
