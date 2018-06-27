# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Test
from .forms import TestUpload


# Create your views here.
def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests' : tests})

def subject_list(request):
    return render(request, 'subject_list.html')

def topic_list(request):
    return render(request, 'topic_list.html')
    
def question_list(request):
    return render(request, 'question_list.html')

def import_question(request):
    return render(request, 'import_question.html')

def delete(request, pk):
    query = Test.objects.get(pk=id)
    query.delete()
    return render(request, 'test_list.html')

def add_test(request):
    if request.method == 'POST':
        test_name = request.POST.get('test_name')
        test_type = request.POST.get('test_type')
        test_date = request.POST.get('test_date')
        test_obj = Test(test_name = test_name, test_type = test_type, test_date = test_date)
        test_obj.save()
        
    return render(request, 'test_list.html')