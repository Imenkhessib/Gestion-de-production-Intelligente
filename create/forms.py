from django import forms
from .models import item, MO, project


class AllForm(forms.ModelForm):
    class Meta:
        model = item
        fields = (
            'item_reference', 'designation', 'quantity', 'cnc', 'router', 'laser_Cutters', 'milling', 'two_d_plan',
            'three_d_plan')
        widgets = {

            'item_reference': forms.TextInput(
                attrs={'id': 'id', 'class': "form-control form-control-user",'placeholder': "Reference" }),
            'designation': forms.TextInput(attrs={'id': 'desig', 'class': "form-control form-control-user",'placeholder': "Designation"}),
            'quantity': forms.NumberInput(
                attrs={'id': 'quantity', 'class': "form-control form-control-user", 'placeholder': "Quantity"}),

        }


class essai(forms.ModelForm):
    class Meta:
        model = project
        fields = ('project_ref', 'project_name', 'client', 'purchase_order', 'project_manager')


class MO_form(forms.ModelForm):
    class Meta:
        model = MO
        fields = "__all__"
