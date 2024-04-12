from django.core.validators import RegexValidator
from django.db import models
from .base import Base
from .country import Country
from .state import State
from .city import City


class User(Base):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True,validators=[
            RegexValidator(
                regex=r'^(\+91)?\d{10}$',
                message="Phone number must be exactly 10 digits and can optionally start with '+91'",
            )
        ])
    user_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user_state = models.ForeignKey(State, on_delete=models.CASCADE,default=0)
    user_city = models.ForeignKey(City, on_delete=models.CASCADE,default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"