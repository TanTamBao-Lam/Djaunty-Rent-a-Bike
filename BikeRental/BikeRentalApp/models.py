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
    
# Rental model
class Rental(models.Model):
    # Bike field is a foreign key to Bike model.
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    
    # Renter field is a foreign key to Renter model.
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    
    # Rent date field.
    date = models.DateField(default=datetime.date.today)
    
    # Price field
    price = models.FloatField(default=0.0)
    
    #str representation
    def __str__(self) -> str:
        return f"Bike: {self.bike.bike_type}_{self.bike.color} - Renter: {self.renter.first_name} {self.renter.last_name} - Date: {self.date} - Price: {self.price}"
    
    # Method for calculating price.
    def calc_price(self) -> float:
        curr_price = BASE_PRICE
        
        # if bike type is Tandem or Electric, there will be surcharge based on vehicle type.
        if self.bike.bike_type == "TA":
            curr_price += TANDEM_SURCHARGE
        if self.bike.bike_type == "EL":
            curr_price += ELECTRIC_SURCHARGE    
        # if renter is vip, discount current price 20%.
        if self.renter.vip_num > 0:
            curr_price *= .8
            
        # set price.
        self.price = curr_price
        

# endregion