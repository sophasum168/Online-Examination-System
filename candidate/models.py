# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
class course(models.Model):
	email = models.EmailField(max_length=120, blank=True, null=True)
	firstname= models.CharField(max_length=120, blank=True, null=True)
	lastname = models.CharField(max_length=120, blank=True, null=True)
	phonenumber = models.CharField(max_length=120, blank=True, null=True)
	country = models.CharField(max_length=120, blank=True, null=True)
	file = models.ImageField(upload_to='profile_image',blank=True)
	image = models.ImageField(upload_to='card_image',blank=True)
	birthday = models.DateField()
	address = models.CharField(max_length=200, blank=True, null=True)
	sname = models.CharField(max_length=300, blank=True, null=True)
	city = models.CharField(max_length=120, blank=True, null=True)

	def __str__(self):
		return str(('FirstName={0}, LastName={1},Email={2},Phone={3},Country={4},Profile={5},Birthday={6},Address={7},SchoolName={8},City={9},IdCard={10}'.format(self.firstname, self.lastname,self.email,self.phonenumber,self.country,self.file,self.birthday,self.address,self.sname,self.city,self.image))
)


class MyUsers(models.Model):
    user=models.OneToOneField(User)
    #created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=120, blank=False, null=False)
    firstname= models.CharField(max_length=120, blank=False, null=False)
    lastname = models.CharField(max_length=120, blank=False, null=False)
    phonenumber = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=False, null=False)
    # file = models.ImageField(upload_to='profile_image',blank=False)
    # image = models.ImageField(upload_to='card_image',blank=False)
    birthday = models.DateField(blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    sname = models.CharField(max_length=300, blank=False, null=False)
    city = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.user.username
# Create your models here.
