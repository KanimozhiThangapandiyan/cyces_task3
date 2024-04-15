from rest_framework.generics import CreateAPIView, UpdateAPIView
from apps.comman.models import State
from apps.comman.serializers import CUStateSerializer
from rest_framework.response import Response

class CreateStateView(CreateAPIView):
    queryset = State.objects.filter(is_deleted=False)
    serializer_class = CUStateSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)

class UpdateStateView(UpdateAPIView):
    queryset = State.objects.filter(is_deleted=False)
    serializer_class = CUStateSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        data = {
            'message': 'successful',
            'data': response.data
        }
        return Response(data, status=response.status_code)
