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

