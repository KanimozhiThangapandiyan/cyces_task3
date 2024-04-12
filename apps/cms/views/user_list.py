from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from apps.comman.models import User
from apps.comman.serializers import UserListSerializer
from rest_framework import filters

class UserViewSet(ListModelMixin,GenericViewSet):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name','last_name','email','phone_number','user_country__country_name','user_state__state_name','user_city__city_name']