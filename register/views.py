# -*- coding: utf-8 -*-

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render	
#from .forms import UploadFileForm
from .forms import FileUpload
#from .forms import UserForm
from .models import Register
from .models import Image
from django.http import HttpResponse
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
		city = request.POST.get('city')
		sname = request.POST.get('sname')
		birthday = request.POST.get('birthday')
		address =request.POST.get('address')
		register_obj=Register(email = email,city=city,sname=sname,birthday=birthday,address=address, firstname = firstname, lastname = lastname, phonenumber = phonenumber, country = country)
		register_obj.save()
		for email in Register.objects.values_list('email', flat=True).distinct():
			Register.objects.filter(pk__in=Register.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()
		# can=Register.objects.all().distinct('email')
		book = FileUpload(request.POST, request.FILES)
		if book.is_valid():
			# book = FileUpload(file=request.FILES['image'])
			book.save()
	        return HttpResponseRedirect('/candidate/')
	else:
	    book = FileUpload()
	
	return render(request,'form.html',{'book':book})

def existemail(request):
    # registered = False

    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     profile_form = FileUpload(data=request.POST)

    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         user.username = user.email
    #         user.save()

    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         profile.email = user.email
    #         profile.save()
    #         user.firstname = profile.firstname
    #         user.last_ame = profile.lastname
    #         user.save()

    #         registered = True
    #         return HttpResponseRedirect('/candidate/')
    #     else:
    #         print user_form.errors, profile_form.errors
    # else:
    #     user_form = UserForm()
    #     profile_form = FileUpload()

    # context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'form.html', context)
	
def candidate(request):
	# c=Register.objects.all()
	# lastSeenId = float('-Inf')
	candidates = Register.objects.all()
	# return HttpResponse(output)
	return render(request,'candidate.html',{'candidates':candidates})

def upload_file(request):
	if request.method == 'POST':
	    form = UploadFileForm(request.POST, request.FILES or None)
	    if form.is_valid():
	            # file is saved
	        form.save()
	        return HttpResponseRedirect('/success/url/')
	else:
	    form = UploadFileForm()

	return render(request, 'candidate.html', {'form': form})

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