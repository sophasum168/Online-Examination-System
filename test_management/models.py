# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# # Create your models here.
class Test(models.Model):
    # candidate_id = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    # admin_id = models.OneToOneField('Admin', on_delete=models.CASCADE)
    test_name = models.TextField(max_length=45)
    test_type = models.TextField(max_length=45)
    test_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.test_name

class Subject(models.Model):
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
    subject_name = models.TextField(max_length=45)
    subject_type = models.TextField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.subject_name

class Topic(models.Model):
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    topic_name = models.TextField(max_length=45)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.topic_name

class Question(models.Model):
    QUESTION_TYPE = (('QCM', 'Multiple Choice'),
                    ('ES','Essay'),
                    )
    topic_id = models.ForeignKey('Topic', on_delete=models.CASCADE)
    quest_type = models.CharField(max_length=3, choices=QUESTION_TYPE, default='QCM')
    question = models.TextField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.question

class Option(models.Model):
    ANSWER = (('T','True'),
            ('F','False'),
            )
    quest_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    option = models.TextField(max_length=100)
    answer = models.CharField(max_length=1, choices=ANSWER, default='F')
    last_update_date = models.DateTimeField()

    def __str__(self):
        return self.option

class Admin(models.Model):
    admin_name = models.TextField(max_length=45)

class Candidate(models.Model):
    candidate_name = models.TextField(max_length=45)