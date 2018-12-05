from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *
# sokmeng
# from verified_email_field.forms import VerifiedEmailField
# from .models import CandiateImage

# class RegisterForm(forms.ModelForm):
# 	class Meta:
# 		model = Register
# 		fields = ['firstname','email','lastname','phonenumber','country']

# 	def clean_email(self):
# 		email=self.cleaned_data.get(email)
# 		email_base, provider = email.split("@")
# 		domain, extension = provider.split(".")
# 		if not domain == 'USC':
# 			raise forms.ValidationError("Please make sure you use your USC email")
# 		if not extension == "com":
# 			raise forms.ValidationError("Please user a valid .COM email address")
# 		return email


class UploadFileForm(forms.ModelForm):
   class Meta:
   	model = Image
   	fields = ['file']
# sokmeng
# class UserForm(forms.ModelForm):
#    class Meta:
#         model = User
#         fields = ('email',)
#    def clean_email(self):
#         # Get the email
#         email = self.cleaned_data['email']
#         # email = self.cleaned_data.get('email')

#         # Check to see if any users already exist with this email as a username.
#         try:
#         	mt = verified_email(email)
#             # match = User.objects.get(email=email)
#         except:
#         	return forms.ValidationError("Email is not in correct format")
#         # except User.DoesNotExist:
#             # Unable to find a user, this is fine
#             # return email

#         # A user was found with this as a username, raise an error.
#         return email
#         # raise forms.ValidationError('This email address is already in use.')

# class FileUpload(forms.ModelForm):
# 	class Meta:
#    		model = Register
#    		fields = ('student_profile','card_id')

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoUpload
        fields = ('file',)
        widgets = {'file': forms.HiddenInput()}


#sokmeng

 # def sendEmail(self, datas):
 # 	link="http://yourdomain.com/activate/"+datas['activation_key']
 #    c=Context({'activation_link':link,'username':datas['username']})
 #    f = open(MEDIA_ROOT+datas['email_path'], 'r')
 #    t = Template(f.read())
 #    f.close()
 #    message=t.render(c)
 #        #print unicode(message).encode('utf8')
 #    send_mail(datas['email_subject'], message, 'yourdomain <no-reply@yourdomain.com>', [datas['email']], fail_silently=False)

 #sokmeng
 # class RegistrationForm(forms.ModelForm):
 # 	email = VerifiedEmailField(label='email', required=True)