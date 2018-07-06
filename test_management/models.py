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

    def __str__(self):
        return self.question_name

class Option(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    option_name = models.TextField(max_length=150)
    answer = models.CharField(max_length=1, choices=ANSWER, default='F')
    last_update_date = models.DateTimeField()

    def __str__(self):
        return self.option_name

class Admin(models.Model):
    admin_name = models.TextField(max_length=45)

class Candidate(models.Model):
    candidate_name = models.TextField(max_length=45)