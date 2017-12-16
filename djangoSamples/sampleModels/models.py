# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
