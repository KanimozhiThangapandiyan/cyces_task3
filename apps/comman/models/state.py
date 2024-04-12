from django.db import models
from .base import Base
from .country import Country
class State(Base):
    state_name = models.CharField(max_length=255)
    state_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.state_name