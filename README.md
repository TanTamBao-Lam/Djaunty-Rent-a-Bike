# Djaunty-Rent-a-Bike
The owners of the Djaunty Rent-a-Bike company have asked that you help them revamp their old paper and pencil method of renting out bikes. They know that you’ve learned about Django models, databases, and “CRUD” — and they’re excited to see you apply your skills.

In your conversation with the owners, you realized that their booking system is rather streamlined. Their bikes are rented for the day at a set price and they mainly care about three things: bikes, renters, and rentals. You can boil it down to a schema like:

**Bike**
*bike_type (Rent-a-Bike offers standard, tandem, and electric bikes)
*color (color of the bike)

**Renter**
* first_name (the first name of the renter)
* last_name (the last name of the renter)
* phone (the phone number of the renter)
* vip_num (renter’s VIP status and number)

**Rental**
* bike (what bike is being rented)
* renter (who is renting the bike)
* date (the date of the rental)
* price (how much does the bike rental cost)

The owners have asked you to solely focus your skills on the models and not worry about the templates or views.

## Instruction: 
### Planning
1. Let’s first think about the schema provided. This step is very important because you should start thinking about the underlying shape of the data needed to support your app.
Before you write any code, check out models.py to see what’s provided.

### Creating the Bike Model

2. Now that you’ve had the chance to think about the program, it’s time to code! Let’s first start by creating a Bike model.

3. You can tell from the provided constants that there are 3 specific types of bikes. Since the Bike will have a field for bike type, this is a great time to implement a choice option.
Inside the Bike class, create 3 constants:
* STANDARD with a value of "ST"
* TANDEM with a value of "TA"
* ELECTRIC with a value of "EL"

4. With the constants set up, you can create a list called BIKE_TYPE_CHOICES that stores tuples. Here’s an example of how the first tuple should look.
* (STANDARD, "Standard")

Create the other two using that example.

5. With the setup out of the way, you can create a character field called bike_type. Provide the arguments:
* a max length of 2,
* choices that only accept values from BIKE_TYPE_CHOICES
* defaults to STANDARD.

6. Bikes also have a color and you should track what colors the rental bikes are.
Add a new field called color which:
* is a character field
* has a max length of 10 characters
* defaults to an empty string ("")

7. You’ve added fields for Bike, but the __str__ method should be overridden.
Define a new __str__ method that returns a string with the bike type and color, like:
> "ST - blue"

### Creating the Renter Model
8. Since Bike is set up, you can create the Renter model now.
Create a new Renter class that has the following fields:
* first_name a character field that has a max length of 30
* last_name a character field with max length of 30
* phone a character field with max length of 15
* vip_num an integer field that defaults to 0

9. Renter should also have a custom __str__ method.
Have the __str__ method return the instance’s first name, last name, and phone as a string. Here’s a sample output:
> Padma Lak - #123-456-7890

### Creating the Rental Model
10. Bike and Renter are set up, the only one left is Rental.
Start with the fields:
* bike which is a foreign key for the Bike model
* * upon the foreign key’s deletion, it should cascade

* renter which is a foreign key for the Renter model
* * upon the foreign key’s deletion, it should cascade

* date a date field which defaults to today’s date (datetime.date.today)
* * price a float field which defaults to 0.0

11. While prices default to 0.0, you’ll need a method to calculate the actual price.
Define a method called calc_price. Inside the function body, create a variable called curr_price with a value of BASE_PRICE.

12. You can now implement the additional charges.
Add the following conditionals:
* If self.bike‘s .bike_type is "TA" , then increase curr_price by TANDEM_SURCHARGE.
* If self.bike‘s .bike_type is "EL" , then increase curr_price by ELECTRIC_SURCHARGE.
* If self.renter‘s .vip_num is greater than 0, then discount curr_price by 20%.

13. Still within the .calc_price() method, finalize the cost of the Rental instance by setting the .price field as curr_price.

### Database Setup
14. Nice, your models are all set up now! This means it’s time to set up the schema in your database.
In the terminal execute the command:
> python3 manage.py makemigrations

If there are any error messages, read through and fix them before proceeding.

15. The migration file now needs to be run to properly set up your database. Run:
> python3 manage.py migrate

### Populating Database and Running Queries
16. To check that your models actually work, make some instances!
Start up the Python shell using:
> python3 manage.py shell

Then, import your models!

17. You’re now set to make instances of your models.
You can first start with Bikes. Remember to add in both bike_type and color fields. Also, you’ll need to save these instances to the database! Try to create ~ 5 Bike instances.

18. Moving on to Renter.
Create ~ 3 Renter instances with the proper field types and save them to the database.

19. With instances of both Bike and Renter in the database, you can now make Rental instances!
Create at least 2 Rental instances that use 2 different Bike objects and 2 different Renter objects. You should practice using querying methods to find the objects you want (e.g. .first(), .get(), .all(), etc.)!

20. Now try to fine-tune your querying using methods like .filter() and .exclude() and even reverse relationship! It’s up to you how you want to practice.

### Finishing up
21. Congratulations! You’ve implemented the models and helped out Djaunty Rent-a-Bike!
Now you can rest easy and let your program take care of the work of tracking bikes, renters, and rentals.
However, if you want to challenge yourself, consider:
* Adding extra fields to the existing models, e.g. an AM/PM field for the Rental model.
* Marking when a Bike is rented and cannot be booked.
* Find out how many rentals one specific person has.
Adding in metadata for the models.
