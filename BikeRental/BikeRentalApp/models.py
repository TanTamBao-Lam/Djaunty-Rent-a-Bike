from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# region models

# bike model
class Bike(models.Model):
    # Bike types
    STANDARD = "ST"
    TANDEM = "TA"
    ELECTRIC = "EL"
    
    # Bike type choices
    BIKE_TYPE_CHOICES = [
        (STANDARD, "Standard"),
        (TANDEM, "Tandem"),
        (ELECTRIC, "Electric")
    ]
    
    # Bike type field.
    bike_type = models.CharField(max_length=10, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    
    # Color field.
    color = models.CharField(max_length=10, default="")
    
    # Overiding str method to return bike type with color.
    def __str__(self) -> str:
        return f"{self.bike_type} - {self.color}"
    
# Renter model
class Renter(models.Model):
    # Renter fields
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    vip_num = models.IntegerField(default=0)
    
    # Renter string rep.
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - #{self.phone}"

# endregion