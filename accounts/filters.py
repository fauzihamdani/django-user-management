import django_filters
from django_filters import DateFilter, CharFilter# add date range filter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte') #gte = greater equal to
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__' # menampilkan semua field yang akan di tampilkan di front end
        exclude = ['customer', 'date_created']