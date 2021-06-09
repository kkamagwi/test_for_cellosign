# from django_filters import rest_framework as filters
import django_filters
from django_filters import DateFilter
from statistical_counters.models import Statistics


# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass


class StatFilter(django_filters.FilterSet):
    # views = CharFilterInFilter(field_name='statics__views', lookup_expr='in')
    start_date = DateFilter(field_name='timestamp', lookup_expr='gte',)
    end_date = DateFilter(field_name='timestamp', lookup_expr='lte',)

    class Meta:
        model = Statistics
        # fields = ['views', 'timestamp']
        fields = ['timestamp']