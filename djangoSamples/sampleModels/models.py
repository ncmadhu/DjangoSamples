# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Birthplace(models.Model):
    """
    Example model for ForeignKey
    """
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

    def __str__(self):
        """
        returns string representation
        """
        return "{0} {1}".format(self.city, self.state)

class Person(models.Model):
    """
    Example for a simple Model with a ForeignKey
    relate_name key is used when querying all the persons
    associate with that foreign key.
    eg. bp = Birthplace(city="Coimbatore", state="Tamil Nadu")
        bp.save()
        new_person = Person(first_name="Madhu", last_name="Deepak", birthplace=bp)
        new_person.save()
        new_person = Person(first_name="John", last_name="Deepak", birthplace=bp)
        new_person.save()
        place = Birthplace.object.get(city='Coimbatore')
        place.people.all()
    If relate_name is not given associations can be accessed by
        place.person_set.all() (<model>_set, where model is your model in lowercase)
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthplace = models.ForeignKey(Birthplace, related_name="people")

    def __str__(self):
        """
        returns string representation of the model
        """
        return self.first_name + " " + self.last_name

class UserProfile(models.Model):
    """
    Example for one to one relationship field
    one to one relationship is similar to many to one relationship except it restricts
    two objects to having unique relationship.
    Example would be a user and user profile
    Sample shell example
    from django.contrib.auth.models import User
    from sampleModels.models import UserProfile
    user = User.objects.all()[0]
    user_profile = UserProfile(user=user, favourite_sport='cricket', favourite_color='black')
    user_profile.save()
    profile = UserProfile.objects.get(user=user)
    profile.user
    sample output: <User: madhuchakravarthy>
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    favourite_sport = models.CharField(max_length=50, help_text="Favourite Sport")
    favourite_color = models.CharField(max_length=50, help_text="Favourite Color")

    def __str__(self):
        return "{0} {1}".format(self.favourite_sport, self.favourite_color)

class ModelYear(models.Model):
    """
    Example for many to many relationship field
    In many to many relationship one model is related to many other models
    In this example in a model year several cars could have been manufactured
    and the same type of car model could have been manufactured in several years
        ----------------                                                 ----------------
        |              |------------------ Car Model 1 ------------------|              |
        | Model year 1 |                   Car Model 2 ------------------| Model year 2 |
        |              |------------------ Car Model 3                   |              |
        ----------------                                                 ----------------
    In tha above example in Model year 1 car model 1 and 3 are manufactured
    and car model 1 is also manufactured in Model year 2
    """
    model_year = models.IntegerField(max_length=4, help_text="Model Year")

    def __str__(self):
        return str(self.model_year)

class Car(models.Model):
    """
    Example for many to many relationship field
    In many to many relationship one model is related to many other models
    eg.
    model_year84 = ModelYear(model_year=1984)
    model_year84.save()
    model_year85 = ModelYear(model_year=1984)
    model_year85.save()
    car = Car(model_name="Punto", manufacturer_name="Fiat")
    car.save()
    car.model_year.add(model_year84)
    car.model_year.add(model_year85)
    car.save()
    anothercar = Car(model_name="Fusion", manufacturer_name="Ford")
    anothercar.save()
    anothercar.model_year.add(model_year85)
    anothercar.save()

    DB SAMPLE OUTPUT:

    djangosamples=> SELECT * FROM "sampleModels_car";
      1 | Punto      | Fiat
      2 | Fusion     | Ford

    djangosamples=> SELECT * FROM "sampleModels_modelyear";
      2 |       1984
      3 |       1985

    djangosamples=> SELECT * FROM "sampleModels_car_model_year";
      1 |      1 |            2
      2 |      1 |            3
      3 |      2 |            3

    djangosamples=>
    """

    model_name = models.CharField(max_length=10, help_text="Model Name")
    manufacturer_name = models.CharField(max_length=256, help_text="Car Manufacturer")
    model_year = models.ManyToManyField(ModelYear, help_text="Model Year")

    def __str__(self):
        return "{0} {1}".format(self.manufacturer_name, self.model_name)
