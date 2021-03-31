from django import forms
from .models import piece

class AllForm(forms.ModelForm):
  class Meta:
   model = piece
   fields = ('product_id','designation','quantity')
   widgets = {
       'product_id': forms.TextInput(attrs={'id': '', 'class': "form-control form-control-user", 'type': "text"}),
       'designation': forms.TextInput(attrs={'id': 'desig', 'class': "form-control form-control-user", 'type': "text"}),
       'quantity': forms.TextInput(attrs={'id': 'quantity', 'class': "form-control form-control-user", 'type': "text"}),
   }
