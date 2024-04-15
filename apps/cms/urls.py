from django.urls import include, path
from rest_framework import routers
from apps.cms.views import UserViewSet,CountryViewSet,StateViewSet,CreateStateView,UpdateStateView,CityViewSet,\
    CreateCityView,UpdateCityView,ImportDataFromCSV,ExportUsersCSV

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'country', CountryViewSet, basename="country")
router.register(r'state', StateViewSet, basename="state")
router.register(r'city', CityViewSet, basename="city")

urlpatterns = [
    path('state/create/', CreateStateView.as_view(), name='state_create'),
    path('state/update/<int:pk>/', UpdateStateView.as_view(), name='state_update'),
    path('city/create/', CreateCityView.as_view(), name='city_create'),
    path('city/update/<int:pk>/', UpdateCityView.as_view(), name='city_update'),
    path('users/export/', ExportUsersCSV.as_view(), name='export_users_csv'),
    path('data/import/', ImportDataFromCSV.as_view(), name='import_data'),
    

] + router.urls