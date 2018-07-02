# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Test, Question
# from .forms import TestUpload
from .forms import NameForm


# Create your views here.
def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests' : tests})

def add_test(request):
    if request.method == 'POST':
        test_name = json.loads(request.POST.get('test_name'))
        test_type = json.loads(request.POST.get('test_type'))
        test_date = json.loads(request.POST.get('test_date'))
        test_date = datetime.strptime(test_date, '%Y-%m-%d').date()
        test_obj = Test(test_name = test_name, test_type = test_type, test_date = test_date)
        test_obj.save()
        return HttpResponseRedirect('/test-management/test/')

def edit_test(request):
    if request.method == 'POST':
        row_id = json.loads(request.POST.get('row_id'))
        test_name = json.loads(request.POST.get('test_name'))
        test_type = json.loads(request.POST.get('test_type'))
        test_date = json.loads(request.POST.get('test_date'))

        test_date = datetime.strptime(test_date, '%Y-%m-%d').date()
        row_id = int(row_id)
        tests = Test.objects.all()
        
        for test_obj in tests:
            if test_obj.id == row_id:
                test_obj.test_name = test_name
                test_obj.test_type = test_type
                test_obj.test_date = test_date
                test_obj.save()
                return HttpResponseRedirect('/test-management/test/')

def delete_test(request):
    if request.is_ajax():
        selected_tests = request.POST['test_list_ids']
        print selected_tests
        selected_tests = json.loads(selected_tests)
        for i, test in enumerate(selected_tests):
            Test.objects.filter(id__in=selected_tests).delete()
        return HttpResponseRedirect('/test-management/test/')
    
def question_list(request):
    questions = Question.objects.all()
    form = NameForm()
    return render(request, 'question_list.html', {'questions' : questions, 'form' : form})

def add_question(request):
    if request.method == 'POST':
        question_name = json.loads(request.POST.get('question_name'))
        question_type = json.loads(request.POST.get('question_type'))
        test_id = json.loads(request.POST.get('test_id'))
        question_obj = Question(question_name = question_name, question_type = question_type, test_id = test_id)
        question_obj.save()
        return HttpResponseRedirect('/test-management/question/')

def edit_question(request):
    return render(request, 'import_question.html')

def delete_question(request):
    return render(request, 'import_question.html')

def import_question(request):
    return render(request, 'import_question.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/question_list/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'question_list.html', {'form': form})