from django import forms

from .models import Image
from .models import Register

# # class RegisterForm(forms.ModelForm):
# # 	class Meta:
# # 		model = Register
# # 		fields = ['firstname','email','lastname','phonenumber','country']
# # 		#exclude =['email']
		
class UploadFileForm(forms.ModelForm):
   class Meta:
   	model = Image
   	fields = ['file']

class FileUpload(forms.ModelForm):
   class Meta:
   	model = Register
   	fields = ['firstname','email','lastname','phonenumber','country','file']
   	  