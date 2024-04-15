from rest_framework.generics import CreateAPIView, UpdateAPIView
from apps.comman.models import Country,State
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
#importing states   
import csv
from django.http import JsonResponse
from rest_framework.views import APIView

class ImportStateFromCSV(APIView):
    def post(self, request):
        if 'file' in request.FILES:
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            # Convert all data in CSV file to lowercase
            reader = csv.DictReader(decoded_file)
            for row in reader:
                # Get or create Country object
                country_name = row['country_name'].lower()
                country, created = Country.objects.update_or_create(country_name=country_name)

                # Create or update State object
                state_name = row['state_name'].lower()
                state, created = State.objects.update_or_create(
                    state_name=state_name,
                    state_country=country,
                )
                print(f"Imported state: {state}")

            return JsonResponse({"message": "States imported successfully"})
        else:
            return JsonResponse({"error": "No CSV file provided"}, status=400)
