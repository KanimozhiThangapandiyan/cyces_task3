# from django.http import HttpResponse
# from django.http import JsonResponse
# import csv
# from apps.comman.models import User

# def export_users_csv(request):
#     success_message = {"message": "Users exported successfully"}
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['First Name', 'Last Name', 'Email', 'Phone Number', 'Country', 'State', 'City'])

#     users = User.objects.filter(is_deleted=False)
#     for user in users:
#         writer.writerow([user.first_name, user.last_name, user.email, user.phone_number,
#                          user.user_country.country_name, user.user_state.state_name, user.user_city.city_name])

#     return JsonResponse(success_message)
from django.http import HttpResponse
import csv
from apps.comman.models import User
from django.views import View

class ExportUsersCSV(View):
    def get(self, request):
        success_message = {"message": "Users exported successfully"}
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Phone Number', 'Country', 'State', 'City'])

        users = User.objects.filter(is_deleted=False)
        for user in users:
            writer.writerow([user.first_name, user.last_name, user.email, user.phone_number,
                             user.user_country.country_name, user.user_state.state_name, user.user_city.city_name])

        return response
    
