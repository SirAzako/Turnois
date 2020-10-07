import django_filters
from django_filters import CharFilter, NumberFilter
from .models import *


class TournamentFilter(django_filters.FilterSet):

    name = CharFilter(field_name='name', lookup_expr='icontains', label='Tournament Name',)
    PpT = NumberFilter(field_name='PpT', lookup_expr='contains', label='Person Per Team')
    PrizeL = NumberFilter(field_name='Prize', lookup_expr="lte")
    PrizeG = NumberFilter(field_name='Prize', lookup_expr="gte")

    class Meta:
        model = Tournament
        fields = ['Tournament_Type']
