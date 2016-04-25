from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=20)
	def __str__(self):
		return self.username

class Mouth(models.Model):
	person = models.ForeignKey(Person)
	mouth = models.IntegerField()
	initial = models.IntegerField()

class Details(models.Model):
	mouth = models.ForeignKey(Mouth)
	day = models.IntegerField()
	cost = models.IntegerField()
	remarks = models.CharField(max_length=40)

