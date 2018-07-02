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
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadWCForm
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
			Register.objects.filter(pk__in=Register.objects.filter(email=email).values_list('id', flat=True)[0:]).delete()
        book = FileUpload(request.POST, request.FILES)
        if book.is_valid():
			# book = FileUpload(file=request.FILES['image'])
			book.save()
			return HttpResponseRedirect('/congratulation/')
        
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

# def save_image(request):
# 	if request.POST:
# 		# save it somewhere
# 		f = open(settings.MEDIA_ROOT + '/webcamimages/someimage.jpg', 'wb')
# 		f.write(request.raw_post_data)
# 		f.close()
# 		# return the URL
# 		return HttpResponse('http://localhost:8080/site_media/webcamimages/someimage.jpg')
# 	else:
# 		return HttpResponse('no data')

def upload_webcam(request):
  print "in upload WBCAM "     
  if request.method == 'POST':
      form = ImageUploadWCForm(request.POST, request.FILES)
      #print "FILES", request.FILES
      if form.is_multipart():
          uploadFile=save_filewc(request.FILES['imagewc'])
          print('vALID iMAGE')
      else:
          print('Invalid image')
  else:
      form = ImageUploadWCForm()   
  return render(request, 'capture_image.html')

def save_filewc(file, path=''):
  filename = "sopha.jpg"
  fd = open('%s/%s' % (MEDIA_ROOT1, str(path) + str(filename)), 'wb')
  print "fd", fd
  print "str(path)",str(path)
  print "str(filename)",str(filename)
  for chunk in file.chunks():
      fd.write(chunk)
  fd.close()