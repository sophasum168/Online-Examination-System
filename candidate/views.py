# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import course

# Create your views here.

def cour(request):
	c = course.objects.all()
	output = ",".join([str (cour) for cour in c])

	return HttpResponse(output)