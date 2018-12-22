# -*- coding: utf-8 -*-
import os, string, random
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from test_management.models import *


from django.conf import settings
from django.core.mail import send_mail
# from django.core.validators import RegexValidator
# from regi.models import *

def get_image_name(instance, filename):
	f, ext = os.path.splitext(filename)
	archivo = '%s%s' % (instance.firstname, ext)
	return os.path.join('webcamimages', archivo)
# Create your models here.

# class CandiateImage(models.Model):
# 	card_id = models.ImageField(upload_to='card_id')
# 	student_profile = models.ImageField(upload_to='student_profile')
	
	
class Register(models.Model):
	# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	email = models.EmailField(max_length=120, blank=False, null=False)
	password = models.TextField(max_length=50,blank=True, null=True)
	firstname= models.CharField(max_length=120, blank=False, null=False)
	lastname = models.CharField(max_length=120, blank=False, null=False)
	phonenumber = models.CharField(blank=False, null=False,max_length=30)
	country = models.CharField(max_length=120, blank=False, null=False)
	card_id = models.FileField(upload_to='card_id', null=False, blank=False)
	student_profile = models.FileField(upload_to='student_profile',null=False, blank=False)
	birthday = models.DateField(blank=False, null=False)
	address = models.CharField(max_length=200, blank=False, null=False)
	sname = models.CharField(max_length=300, blank=False, null=False)
	city = models.CharField(max_length=120, blank=False, null=False)
	score = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	taken_test = models.BooleanField(default=False)
	
	
	
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
				self.message = "Dear Candidate, \nThis is a reminder that your password to login to KIT examination is: " + self.password + "\n\nBest Regards,\nKIT Teams"
				# send email, password to candidate
				send_mail(
    						'KIT Register Credential',
    						self.message,
    						'admin_email',
    						[self.email],
    						fail_silently=False,
				)
				messages.add_message(request, messages.SUCCESS, "Successfully registered!")
				return context
		else:
			if request.update == True:
				super(Register, self).save(*args, **kwargs)
				return messages.add_message(request, messages.SUCCESS, "Successfully updated!")
			return messages.add_message(request, messages.ERROR, "Your email is already registered. You can only register for the exam once!")

    #Authenticate user login credential from Desktop application
	def login_authentication(self, email, password):
	   	user = Register.objects.get(email = email, password = password)
		try:
			user = Register.objects.get(email = email, password = password)
			if user.taken_test == False:
				return True
			return False
		except Register.DoesNotExist:
			return False
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
		
class Image(models.Model):
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

class CandidateAnswer(models.Model):
	candidate_id = models.ForeignKey('Register', on_delete=models.CASCADE)
	question_id = models.ForeignKey('test_management.Question', on_delete=models.CASCADE)
	essay_answer = models.TextField(blank=True, null=True)
	selected_option = models.TextField(blank=True, null=True)