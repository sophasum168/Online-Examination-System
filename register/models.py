# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Register(models.Model):
	email = models.EmailField(max_length=120, blank=True, null=True)
	firstname= models.CharField(max_length=120, blank=True, null=True)
	lastname = models.CharField(max_length=120, blank=True, null=True)
	phonenumber = models.CharField(max_length=120, blank=True, null=True)
	country = models.CharField(max_length=120, blank=True, null=True)
	file = models.ImageField(upload_to='images/%Y/%m/%d/')
	
	def __str__(self):
		return str(('FirstName={0}, LastName={1},Email={2},Phone={3},Country={4},Image={5}'.format(self.firstname, self.lastname,self.email,self.phonenumber,self.country,self.file))
)
		# return self.firstname
		# return self.lastname
		# return self.phonenumber
		# return self.country	
		
class Image(models.Model):
	# imageid = models.AutoField()
   	# title = models.CharField(max_length=100)
   	file = models.ImageField(upload_to='images/%Y/%m/%d/')

   	def __str__(self):
   		return str(self.file)
