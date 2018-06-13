# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render
from .models import Test
from django_tables2 import RequestConfig


# Create your views here.
def test_list(request):
    list = Test.objects.all()
    return render(request, 'test_list.html',{'list':list})

def subject_list(request):
    return render(request, 'subject_list.html')

def topic_list(request):
    return render(request, 'topic_list.html')
    
def question_list(request):
    return render(request, 'question_list.html')

def import_question(request):
    return render(request, 'import_question.html')




