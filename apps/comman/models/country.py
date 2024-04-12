from django.db import models
from .base import Base

class Country(Base):
    country_name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.country_name