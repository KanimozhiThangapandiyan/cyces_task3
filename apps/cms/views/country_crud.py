from rest_framework.viewsets import ModelViewSet
from apps.comman.models import Country
from apps.comman.serializers import CountrySerializer
from rest_framework import filters

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.filter(is_deleted=False)
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country_name']
