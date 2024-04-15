from rest_framework.viewsets import ModelViewSet
from apps.comman.models import State
from apps.comman.serializers import StateSerializer
from rest_framework import filters
from rest_framework.response import Response

class StateViewSet(ModelViewSet):
    queryset = State.objects.filter(is_deleted=False)
    serializer_class = StateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['state_name','state_country__country_name']

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

