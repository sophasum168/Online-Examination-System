# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *
from .forms import QuestionForm, OptionForm
from .serializers import QuestionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
# from .forms import TestUpload


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
        selected_tests = json.loads(selected_tests)
        for i, test in enumerate(selected_tests):
            Test.objects.filter(id__in=selected_tests).delete()
        return HttpResponseRedirect('/test-management/test/')
    
def question_list(request):
    questions = Question.objects.all()
    questionForm = QuestionForm()
    optionForm = OptionForm()
    return render(request, 'question_list.html', {'questions' : questions, 'questionForm' : questionForm, 'optionForm' : optionForm })

def add_question(request):
    if request.method == 'POST':
        question_name = json.loads(request.POST.get('question_name'))
        question_type = json.loads(request.POST.get('question_type'))
        test_id = json.loads(request.POST.get('test_id'))
        question_obj = Question(question_name = question_name, question_type = question_type, test_id = Test.objects.get(id=test_id))
        question_obj.save()
        
        option_rows = json.loads(request.POST.get('option_rows'))
        for option in option_rows:
            option_obj = Option()
            option_obj.question_id = question_obj
            option_obj.option_name = option
            option_obj.answer = option_rows[option]
            option_obj.save()
        return HttpResponseRedirect('/test-management/question/')

def edit_question(request):
    context = dict()
    if request.method == 'GET':
        row_id = request.GET.get('row_id')
        question_obj = Question()
        question = question_obj.edit_question(row_id)
        question_form = QuestionForm(initial={'question_name': question[0]['question_name'],
                                            'question_type': question[0]['question_type'],
                                            'test_id': question[0]['test_id']}, auto_id=False).__str__()
        option_form = ""
        if question[1]:
            cont = dict()
            options_form = []
            for option in question[1]:
                option_form = OptionForm(initial={'option_name': option['option_name'],
                                                    'answer': option['answer']})
                options_form.append(option_form)
            cont.update({'options': options_form})
            option_form = render_to_string('include/question_option_row.html', cont)
        context.update({
            'question_form': question_form,
            'option_form': option_form,
        })          
        return JsonResponse(context)
    elif request.method == 'POST':
        row_id = json.loads(request.POST.get('row_id'))
        test_id = json.loads(request.POST.get('test_id'))
        question_type = json.loads(request.POST.get('question_type'))
        question_name = json.loads(request.POST.get('question_name'))
        option_rows = json.loads(request.POST.get('option_rows'))
        kwargs = {"test_id":test_id, "question_type":question_type, "question_name":question_name, "option_rows":option_rows}
        question_obj = Question()
        question = question_obj.edit_question_save(row_id, **kwargs)
        return HttpResponseRedirect('/test-management/question/')

def delete_question(request):
    if request.is_ajax():
        selected_questions = request.POST['question_list_ids']
        selected_questions = json.loads(selected_questions)
        for i, test in enumerate(selected_questions):
            Question.objects.filter(id__in=selected_questions).delete()
        return HttpResponseRedirect('/test-management/question/')

def import_question(request):
    return render(request, 'import_question.html')

@csrf_exempt
def get_test_questions(request):
    """
    API to get a list of questions
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
