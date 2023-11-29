import django_filters
from django_filters.rest_framework import FilterSet

from subscribtions.models import Subscription, Category


class SubsFilter(FilterSet):
    category = django_filters.ModelMultipleChoiceFilter(
        field_name='category__name',
        to_field_name='name',
        queryset=Category.objects.all())

    class Meta:
        model = Subscription
        fields = ['author', 'category']
