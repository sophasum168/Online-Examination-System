# -*- coding: utf-8 -*-
import os, string, random
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

def get_image_name(instance, filename):
	f, ext = os.path.splitext(filename)
	archivo = '%s%s' % (instance.firstname, ext)
	return os.path.join('webcamimages', archivo)
# Create your models here.

class Register(models.Model):
	# user=models.OneToOneField(User)
    # updated_at = models.DateTimeField(auto_now=True)
	email = models.EmailField(max_length=120, blank=False, null=False)
	password = models.TextField(blank=True, null=True)
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
	created_at = models.DateTimeField(auto_now_add=True)
	
	#Override save method for Register model for auto generating random login password
	def save(self, request, *args, **kwargs):
		if not Register.objects.filter(email = self.email):
			if self.password is None:
				self.password = self.password_generator()
				super(Register, self).save(*args, **kwargs)
				context = {
					'email' : self.email,
					'password' : self.password,
					}
				messages.add_message(request, messages.SUCCESS, "Successfully registered!")
				return context
		else:
			return messages.add_message(request, messages.ERROR, "Your email is already registered. You can only register for the exam once!")

    #Authenticate user login credential from Desktop application
	def login_authentication(self, email, password):
		if Register.objects.filter(email = email, password = password):
			return True
		return False

    #Generate random login password for candidate
	def password_generator(self, size=30, chars=string.ascii_letters + string.digits):
		return ''.join(random.choice(chars) for i in range(size))

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

@python_2_unicode_compatible
class VideoUpload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(
        upload_to='temp_videos',
        blank=True,
        null=True,
        verbose_name=u'File')

    def __str__(self):
        return self.uploaded_at
