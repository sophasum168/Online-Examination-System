# -*- coding: utf-8 -*-

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render	
from .forms import UploadFileForm
from .forms import FileUpload
from .models import Register
from .models import Image
from django.http import HttpResponseRedirect
#from .forms import SignUpForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		phonenumber = request.POST.get('phonenumber')
		country = request.POST.get('country')
		# images = register.POST.get('file')
		register_obj=Register(email = email, firstname = firstname, lastname = lastname, phonenumber = phonenumber, country = country)
		register_obj.save()
		book = FileUpload(request.POST, request.FILES)
		if book.is_valid():
			# book = FileUpload(file=request.FILES['image'])
			book.save()
	        return HttpResponseRedirect('/register/')
	else:
	    book = FileUpload()
	
	return render(request,'form.html',{'book':book})
	
def register_view(request):
	return render(request,'form.html',{})

def logout_view(request):
	return render(request,'form.html',{})

def upload_file(request):
	if request.method == 'POST':
	    form = UploadFileForm(request.POST, request.FILES or None)
	    if form.is_valid():
	            # file is saved
	        form.save()
	        return HttpResponseRedirect('/success/url/')
	else:
	    form = UploadFileForm()
	return render(request, 'upload.html', {'form': form})

# def upload(request):
#     if request.method == 'POST':
#         handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
#         return HttpResponse("Successful")
 
#     return HttpResponse("Failed")
 
# def handle_uploaded_file(file, filename):
#     if not os.path.exists('upload/'):
#         os.mkdir('upload/')
 
#     with open('upload/' + filename, 'wb+') as destination:
#         for chunk in file.chunks():
#             destination.write(chunk)