import django_filters


def past_offer_filter_method(queryset, name, value):

    queryset = queryset.filter(
        field__relation_field__in=SOME_CHOICES
    )
    return queryset


def select_view_filter_method(queryset, name, value):

    queryset = queryset.filter(
        field__relation_field=value
    )
    return queryset


def select_3d_floor_filter_method(queryset, name, value):
    queryset = queryset.filter(
        field__relation_field=value
    )
    return queryset


class PropertyListFilter(django_filters.FilterSet):
    min_budget = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_budget = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    bedroom = django_filters.NumberFilter(field_name="bedroom", lookup_expr='lte')
    endData = django_filters.DateFilter(field_name="endData", lookup_expr='lte')
    past = django_filters.CharFilter(method=past_offer_filter_method)
    select_view = django_filters.CharFilter(method=select_view_filter_method)
    floor = django_filters.CharFilter(method=select_3d_floor_filter_method)

    class Meta:
        model = Model
        fields = ['price', 'bedroom', 'areaId', 'endData', "property_offer"]
