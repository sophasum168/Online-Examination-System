# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import course
from .models import MyUsers
# from .forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def cour(request):
	c = course.objects.all()
	output = ",".join([str (cour) for cour in c])

	return HttpResponse(output)

def index(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.password = ""
            user.username = user.email
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.save()

            # user.firstname = profile.firstname
            # user.lastname = profile.lastname
            # user.save()

            registered = True
            return HttpResponseRedirect('/register/')
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'register.html', context)