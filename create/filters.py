import django_filters
from .models import *
from .models import piece

class filterr(django_filters.FilterSet):
    class Meta:
        model = MO
        fields = ('project_Reference', 'state_MO')


class filterrr(django_filters.FilterSet):
    class Meta:
        model = piece
        fields = ('thickness', 'num_MO')

