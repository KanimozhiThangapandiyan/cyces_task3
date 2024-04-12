from django.db import models
from .base import Base
from .country import Country
from .state import State

class City(Base):
    city_name = models.CharField(max_length=255)
    city_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name
