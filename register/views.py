# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render	
#from .forms import UploadFileForm
from .forms import FileUpload
from django.views.decorators.csrf import csrf_exempt
from .models import Register
from django.views.decorators.csrf import csrf_exempt
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
			Register.objects.filter(pk__in=Register.objects.filter(email=email).values_list('id', flat=True)[0:]).delete()
        book = FileUpload(request.POST, request.FILES)
        if book.is_valid():
			# book = FileUpload(file=request.FILES['image'])
			book.save()
			return HttpResponseRedirect('/candidate/')
        	
	return render(request,'form.html',{'book':book})

def congratulation(request):
    return render(request, 'capture.html')
	
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

class SaveImage(TemplateView):

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		self.filename = self.kwargs['cedula']+'.jpg'
		return super(SaveImage, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/webcamimages/'+ self.filename, 'wb')
		f.write(request.body)
		f.close()
		# return the URL
		return HttpResponse("/media/webcamimages/" + self.filename)

	def get(self, request, *args, **kwargs):
		return HttpResponse('No esta pasando el POST')

