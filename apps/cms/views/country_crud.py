from rest_framework.viewsets import ModelViewSet
from apps.comman.models import Country
from apps.comman.serializers import CountrySerializer
from rest_framework import filters
from rest_framework.response import Response

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.filter(is_deleted=False)
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country_name']

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
