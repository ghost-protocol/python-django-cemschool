# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Student(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100, blank=True)
    dateofbirth = models.DateTimeField(default=datetime.datetime.now)
    hometown = models.CharField(max_length=100)
    # mother_tongue = models.CharField(max_length=100)
    # father_tongue = models.CharField(max_length=100)
    date_admission = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
    	return "%s %s %s" % (self.surname, self.firstname, self.othername)

class Parent(models.Model):
	TITLE_CHOICES=(
		('MR','MR'),
		('MRS','MRS'),
		('MISS','MISS'),
		('DR','DR')
	)
	# LIVING_CHOICES=(
	# 	'Both Parents','Both Parents',
	# 	'Mother','Mother',
	# 	'Father','Father',
	# 	'Guardian','Guardian'
	# )
	student = models.ForeignKey(Student)
	title = models.CharField(max_length=10, choices=TITLE_CHOICES)
	relationship = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	othername = models.CharField(max_length=100, blank=True)
	address = models.CharField(max_length=100)
	residence = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100)
	education_level = models.CharField(max_length=100)
	# number_wives = models.IntegerField()
	# living = models.CharField(choices=LIVING_CHOICES)
	children_home = models.IntegerField()

	def __unicode__(self):
		return "%s | %s %s" % (self.student, self.surname, self.firstname)

class Medical(models.Model):
	student = models.ForeignKey(Student)
	whooping_cough = models.DateTimeField(default=datetime.datetime.now)
	diphteria = models.DateTimeField(default=datetime.datetime.now)
	tetanus = models.DateTimeField(default=datetime.datetime.now)
	measels = models.DateTimeField(default=datetime.datetime.now)
	medical_officer_remarks = models.CharField(max_length=500)

	def __unicode__(self):
		return "%s" % (self.student)
