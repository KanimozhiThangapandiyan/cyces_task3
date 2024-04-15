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

#importing countries   
import csv
from django.http import JsonResponse
from rest_framework.views import APIView

class ImportCountryFromCSV(APIView):
    def post(self, request):
        if 'file' in request.FILES:
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            # Convert all data in CSV file to lowercase
            reader = csv.DictReader(decoded_file)
            for row in reader:
                # Create or update Country object
                country, created = Country.objects.update_or_create(
                    country_name=row['country_name'].lower()
                )
                print(f"Imported country: {country}")

            return JsonResponse({"message": "Countries imported successfully"})
        else:
            return JsonResponse({"error": "No CSV file provided"}, status=400)
