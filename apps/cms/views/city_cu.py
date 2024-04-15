from rest_framework.generics import CreateAPIView, UpdateAPIView
from apps.comman.models import City
from apps.comman.serializers import CUCitySerializer
from rest_framework.response import Response

class CreateCityView(CreateAPIView):
    queryset = City.objects.filter(is_deleted=False)
    serializer_class = CUCitySerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)

class UpdateCityView(UpdateAPIView):
    queryset = City.objects.filter(is_deleted=False)
    serializer_class = CUCitySerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)
