from rest_framework.generics import CreateAPIView, UpdateAPIView
from apps.comman.models import Country,State,City
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
#importing Cities  
import csv
from django.http import JsonResponse
from rest_framework.views import APIView

class ImportCityFromCSV(APIView):
    def post(self, request):
        if 'file' in request.FILES:
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            # Convert all data in CSV file to lowercase
            reader = csv.DictReader(decoded_file)
            for row in reader:
                country_name = row['country_name'].lower()
                country, created = Country.objects.get_or_create(country_name=country_name)

                # Get or create State object
                state_name = row['state_name'].lower()
                state, created = State.objects.get_or_create(
                    state_name=state_name,
                    state_country=country,
                )

                # Create or update City object
                city_name = row['city_name'].lower()
                city, created = City.objects.update_or_create(
                    city_name=city_name,
                    city_country=country,
                    city_state=state,
                )
                print(f"Imported city: {city}")

            return JsonResponse({"message": "Cities imported successfully"})
        else:
            return JsonResponse({"error": "No CSV file provided"}, status=400)
