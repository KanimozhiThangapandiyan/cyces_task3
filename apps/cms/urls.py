from django.urls import include, path
from rest_framework import routers
from apps.cms.views import UserViewSet,CountryViewSet,StateViewSet,CityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'country', CountryViewSet, basename="country")
router.register(r'state', StateViewSet, basename="state")
router.register(r'city', CityViewSet, basename="city")

urlpatterns = []+router.urls