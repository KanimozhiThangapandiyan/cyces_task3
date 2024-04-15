import csv
from django.http import JsonResponse
from django.views import View
from apps.comman.models import Country, State, City
from rest_framework.views import APIView
from rest_framework.response import Response

#from django.views.decorators.csrf import csrf_exempt
# from django.middleware.csrf import get_token
# from django.views.decorators.csrf import ensure_csrf_cookie


class ImportDataFromCSV(APIView):
    def post(self, request):
        if 'file' in request.FILES:
            csv_file = request.FILES['file']

            # Call the import_data_from_csv function to process the file
            response = self.import_data_from_csv(csv_file)
            return response
        else:
            return response({"error": "No CSV file provided"}, status=400)
    
    def import_data_from_csv(self, csv_file):
        success_message = {"message": "Data imported successfully"}
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            # Create or get Country object
            country, created = Country.objects.get_or_create(country_name=row['country_name'])

            # Create or get State object
            state, created = State.objects.get_or_create(state_name=row['state_name'], state_country=country)

            # Create City object
            city = City.objects.create(
                city_name=row['city_name'],
                city_country=country,
                city_state=state
            )
            print(f"Created city: {city}")

        return Response(success_message)