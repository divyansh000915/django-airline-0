from django.db import models

#Django designed with wanting to interact with databases in mind
# Create your models here. Here we will define classes that are going to define the types of datawe will be able to store inside the database for this app
#very similar to SQLAlchemy
class Airport(models.Model): #class flight which is going to be type of model
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    #on_delete=models.CASCADE is a speacial function of handling the situation of what happens when you delete a airport, there can be multiple ways of 
    #handling this situation, some may give error that hey, it's aForeign Key constraint, don't delete, for others, it maybe like delete all those flights
    #which have origin as that id. Here with CASCADE, the latter one is followed
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    #here we are not telling what column of Airport is related to origin or destination, just telling htat origin and destinations are airport, 
    #leaving rest to django about how this association takes place and how these relationships work
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")#here linked passengers and Flights table through a many to many relationship 
    #as one flight can be associated with many passengers and one passenger may book tickets for multiple flights. Conventional way out would be to have a
    #3rd table that stores passenger name and flights associated with him. But in django can do it without needing to explicitly creating a new table
    #blank = True means it maybe possible that the passenger is not associated with any of the flight

    #if see the actual sql working behind this when run this migration, we can see that internally 2 tables are created :
    #1. The flights_passenger table having and id(auto), first and last name
    #2. The flights_passenger_flights table having an id(auto, primary key), passenger_id(referes id of passenger table), and flights_id(refers id of flights table)
    # so django basically automatically finds out what sql it needs to run

    def __str__(self):
        return f"{self.first} {self.last}"
