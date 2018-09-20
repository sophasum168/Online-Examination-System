# -*- coding: utf-8 -*-
import logging, ast, json
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.core.files.base import File
from django.shortcuts import render	
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *
from .forms import *
from test_management.models import *

# Create your views here.
def register(request):
	if request.method == 'GET':
		return render(request,'form.html')
	elif request.method == 'POST':
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
		context = register_obj.save(request)
		return render(request, 'congratulation.html', {'context' : context})
	
def candidate(request):
	# c=Register.objects.all()
	# lastSeenId = float('-Inf')
	candidates = Register.objects.all()
	# return HttpResponse(output)
	return render(request,'candidate.html',{'candidates':candidates})
	
def edit_candidate(request):
    context = dict()
    if request.method == 'GET':
        row_id = request.GET.get('row_id')
        candidate_obj = Register.objects.get(id = row_id)
        context.update({
            'first_name': candidate_obj.firstname,
            'last_name': candidate_obj.lastname,
			'email': candidate_obj.email,
			'phonenumber': candidate_obj.phonenumber,
			'city': candidate_obj.city,
			'country': candidate_obj.country,
			'birthday': candidate_obj.birthday,
			'address': candidate_obj.address,
			'score': candidate_obj.score,
			'created_at': candidate_obj.created_at,
        })          
        return JsonResponse(context)

def delete_candidate(request):
    if request.is_ajax():
        selected_candidates = request.POST['candidate_id']
        selected_candidates = json.loads(selected_candidates)
        for i, test in enumerate(selected_candidates):
            Register.objects.filter(id__in=selected_candidates).delete()
        return HttpResponseRedirect('/candidate/')

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

@csrf_exempt
def video_upload(request):
	if request.method == 'POST':
		form = VideoUploadForm(request.POST, request.FILES)
		if form.is_valid():
			newform = form.save(commit=False)
			djfile = File(request.FILES['data_blob'])
			newform.file.save(request.FILES['data_blob'].name, djfile)
			newform.save()

			# convert to fix the duration of video
			file_path = newform.file.path
			os.system(
				"/usr/bin/mv %s %s" % (
					file_path, (file_path + '.original'))
			)
			os.system(
				"/usr/bin/ffmpeg -i %s -c copy -fflags +genpts %s" % (
					(file_path + '.original'), file_path)
			)

			return HttpResponse({"status":"ok"})
		else:
			form = UploadFileForm()
		return HttpResponse({"status":"ok"})

class SaveImage(TemplateView):
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		self.filename = self.kwargs['firstname']+'.jpg'
		return super(SaveImage, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/webcamimages/'+ self.filename, 'wb')
		f.write(request.body)
		f.close()
		# return the URL
		return HttpResponse("/media/webcamimages/" + self.filename)

	def get(self, request, *args, **kwargs):
		return HttpResponse('No Data POST')

@csrf_exempt
def submit_answer(request):
	"""
	API to get the input answers from desktop application
	"""
	if request.method == 'POST':
		data = JSONParser().parse(request)
		question_data  = data['answer']
		if Register.objects.get(email = data['email']):
			user_id = Register.objects.get(email = data['email'])
			for question in question_data:
				question_id = Question.objects.get(id = question['id'])
				answer = CandidateAnswer()
				if question['question_type'] == 'QCM':
					answer.candidate_id = user_id
					answer.question_id = question_id
					if question['selected_option']:
						answer.selected_option = question['selected_option']
						correct_answer = Option.objects.get(question_id = question_id, answer='T').id
						if int(answer.selected_option) == int(correct_answer):
							user_id.score += 1
						answer.save()
				else:
					if question['essay_answer']:
						answer.candidate_id = user_id
						answer.question_id = question_id
						answer.essay_answer = question['essay_answer']
						answer.save()
			user_id.taken_test = True
			request.update=True
			user_id.save(request)
		return HttpResponse({"status":"ok"})
	return HttpResponse({"status":"ok"})

# @csrf_exempt
# def save_image(self, *args, **kwargs):
# 	self.filename = self.kwargs['firstname']+'.jpg'
# 	# return dispatch(*args, **kwargs)
# 	f = open(settings.MEDIA_ROOT + '/webcamimages/'+ self.filename, 'wb')
# 	f.write(request.body)
# 	f.close()
# 	# f.save()
# 	# return the URL
# 	return HttpResponse("/media/webcamimages/" + self.filename)

	# else:
	# 	return HttpResponse('no data')
