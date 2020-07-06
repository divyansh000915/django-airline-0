#admin is one of the most powerful feature of django hen it comes to add or manipulate data inside database, makes it very easy
#instead of lgin to shell, write python code to do it. To do it from your website, even flask has a long job for that. First create a page showing all
#available flights, list out the airports, choose a valid origin and destination, quite a bit of code. Nowbdjango is designed to be used with a lot of 
#different types of data. So djago comes in with a built in app called admin to add and modify existing data

from django.contrib import admin

from .models import Airport, Flight, Passenger #bcz we want our admin interface to know somwthing about Airport, Flight, Passenger

# Register your models here.

class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

#using django admin app, it's very easy to udate existing models, and data inside models

admin.site.register(Airport)#registering these models with admin site, through which we will be able to change and manipulate data
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)

#to access the admin site, need to login to admin site. Now in Flask, if we want to login, need to make the login interface ourselves, 
# design a user's table, figure out how to let users be authenticated, for this we can easily create users in django : python manage.py createsuperuser
#can modify admin.py as per our need, can customise it as well, like prevent creating a new flight from Paris to Paris.
#this admin interface is not meant to be used by all users of your website, only the contact managers
