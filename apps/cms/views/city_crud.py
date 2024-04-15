from rest_framework.viewsets import ModelViewSet
from apps.comman.models import City
from apps.comman.serializers import CitySerializer
from rest_framework import filters 
from rest_framework.response import Response


class CityViewSet(ModelViewSet):
    queryset = City.objects.filter(is_deleted=False)
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city_name','city_country__country_name','city_state__state_name']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)
    def delete(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)