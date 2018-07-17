# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# # Create your models here.
ANSWER = (
    ('T','True'),
    ('F','False'),
)

QUESTION_TYPE = (
    ('QCM', 'Multiple Choice'),
    ('ES','Essay'),
)

class Test(models.Model):
    # candidate_id = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    # admin_id = models.OneToOneField('Admin', on_delete=models.CASCADE)
    test_name = models.TextField(max_length=45)
    test_type = models.TextField(max_length=45)
    test_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.test_name

class Question(models.Model):
    
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPE, default='QCM')
    question_name = models.TextField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)

    def edit_question(self, row_id):
        question_obj = Question.objects.get(id = row_id)
        option_obj = Option()
        option = option_obj.edit_option(question_obj.id)
        question = {}
        question['test_id'] = question_obj.test_id.id
        question['test_name'] = question_obj.test_id.test_name
        question['question_type'] = question_obj.question_type
        question['question_name'] = question_obj.question_name
        if question['question_type'] == 'QCM':
            return question, option
        else:
            return question, None

    def __str__(self):
        return self.question_name

class Option(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    option_name = models.TextField(max_length=150)
    answer = models.CharField(max_length=1, choices=ANSWER, default='F')
    last_update_date = models.DateTimeField(auto_now_add=True)

    def edit_option(self, question_id):
        options = Option.objects.filter(question_id = question_id).values('option_name', 'answer')
        if options != None:
            option = []
            for obj in options:
                option.append(obj)
            return option
        else:
            return None

    def __str__(self):
        return self.option_name

class Admin(models.Model):
    admin_name = models.TextField(max_length=45)

class Candidate(models.Model):
    candidate_name = models.TextField(max_length=45)