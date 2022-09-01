from django_filters import rest_framework as filters
from cars.models import Car


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class CarFilter(filters.FilterSet):
    queryset = Car.objects.all()
    category = CharFilterInFilter(field_name='category', lookup_expr='in')
    engine = filters.RangeFilter()

    class Meta:
        model = Car
        fields = ['category']