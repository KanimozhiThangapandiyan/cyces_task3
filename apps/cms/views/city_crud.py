from rest_framework.viewsets import ModelViewSet
from apps.comman.models import City
from apps.comman.serializers import CitySerializer
from rest_framework import filters


class CityViewSet(ModelViewSet):
    queryset = City.objects.filter(is_deleted=False)
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city_name','city_country__country_name','city_state__state_name']