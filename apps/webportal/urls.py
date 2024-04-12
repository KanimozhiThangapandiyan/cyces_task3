from django.urls import include, path
from rest_framework import routers
from apps.comman.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'register', UserViewSet, basename="user")

urlpatterns = []+router.urls
