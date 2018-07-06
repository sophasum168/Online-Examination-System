# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import os

def get_image_name(instance, filename):
	f, ext = os.path.splitext(filename)
	archivo = '%s%s' % (instance.firstname, ext)
	return os.path.join('webcamimages', archivo)
# Create your models here.

class Register(models.Model):
	# user=models.OneToOneField(User)
	created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
	email = models.EmailField(max_length=120, blank=False, null=False)
	firstname= models.CharField(max_length=120, blank=False, null=False)
	lastname = models.CharField(max_length=120, blank=False, null=False)
	phonenumber = models.CharField(max_length=120, blank=True, null=True)
	country = models.CharField(max_length=120, blank=False, null=False)
	file = models.ImageField(upload_to=get_image_name, blank=True, null=True)
	image = models.ImageField(upload_to='card_image',blank=False)
	birthday = models.DateField(blank=False, null=False)
	address = models.CharField(max_length=200, blank=False, null=False)
	sname = models.CharField(max_length=300, blank=False, null=False)
	city = models.CharField(max_length=120, blank=False, null=False)

	def __unicode__(self):
		return self.firstname
	@models.permalink
	def get_absolute_url(self):
		return ('Register', [str(self.id)])

	def _get_full_name(self):
		"Retorna los nombres completos de Persona"
		return '%s %s' % (self.city, self.address)

	full_name = property(_get_full_name)
		#return str(('FirstName={0}, LastName={1},Email={2},Phone={3},Country={4},Profile={5},Birthday={6},Address={7},SchoolName={8},City={9},IdCard={10}'.format(self.firstname, self.lastname,self.email,self.phonenumber,self.country,self.file,self.birthday,self.address,self.sname,self.city,self.image))
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
