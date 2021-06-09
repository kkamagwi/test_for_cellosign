import django_filters
from django_filters import DateFilter
from statistical_counters.models import Statistics


class StatFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='timestamp', lookup_expr='gte',)
    end_date = DateFilter(field_name='timestamp', lookup_expr='lte',)

    class Meta:
        model = Statistics
        fields = ['timestamp']