# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

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
    test_name = models.TextField(max_length=45)
    test_type = models.TextField(max_length=45)
    test_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)

    def add_test(self, **kwargs):
        test_obj = Test()
        test_date = datetime.strptime(kwargs["test_date"], '%m/%d/%Y').date()
        test_obj.test_name = kwargs["test_name"]
        test_obj.test_type = kwargs["test_type"]
        test_obj.test_date = test_date
        test_obj.save() 
        test_id = test_obj.id
        return test_id
    
    def __str__(self):
        return self.test_name.encode('utf8')

class Question(models.Model):
    
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPE, default='QCM')
    question_name = models.TextField(max_length=250)
    img_option = models.FileField(upload_to='question_img', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def add_question(self, test_id, **kwargs):
        question_obj = Question()
        question_obj.test_id = Test.objects.get(id = test_id)
        question_obj.question_type = kwargs['question_type']
        question_obj.question_name = kwargs['question_name']
        try:
            question_obj.img_option = kwargs['question_img']
        finally:
            question_obj.save()

            question_id = question_obj.id
            option_context = {
                        "option":kwargs['option'],
                        "answer":kwargs['answer']
                    }
            if kwargs['question_type'] == "QCM":
                option = Option()
                option.add_option(question_id, **option_context)
            return question_id

    def edit_question(self, row_id):
        question_obj = Question.objects.get(id = row_id)
        option_obj = Option()
        option = option_obj.edit_option(question_obj.id)
        question = {}
        question['test_id'] = question_obj.test_id.id
        question['test_name'] = question_obj.test_id.test_name
        question['question_type'] = question_obj.question_type
        question['question_name'] = question_obj.question_name
        try:
            question['img_option'] = question_obj.img_option
        except Exception as e:
            print e
        if question['question_type'] == 'QCM':
            return question, option
        else:
            return question, None
    
    def edit_question_save(self, row_id, *args, **kwargs):
        test_id = Test.objects.get(id = int(kwargs['test_id']))
        question_obj = Question.objects.get(id = row_id)
        question_obj.test_id = test_id
        question_obj.question_type = kwargs['question_type']
        question_obj.question_name = kwargs['question_name']
        if kwargs['question_img']:
            question_obj.img_option = kwargs['question_img']
        question_obj.save()
        ###Add condition for type 'QCM'
        if kwargs['option_imgs']:
            kwargs = {"options":kwargs['option_rows'], "option_imgs":kwargs['option_imgs']}
        else:
            kwargs = {"options":kwargs['option_rows']}
        option_obj = Option()
        option_obj.edit_option_save(row_id, **kwargs)
        return None   

    def __str__(self):
        return self.question_name.encode('utf8')

class Option(models.Model):
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    option_name = models.TextField(max_length=150, blank=True, null=True)
    answer = models.CharField(max_length=1, choices=ANSWER, default='F')
    img_option = models.FileField(upload_to='option_img', blank=True, null=True)
    last_update_date = models.DateTimeField(auto_now_add=True)

    def add_option(self, question_id, **kwargs):
        if kwargs['answer'] == 't' or kwargs['answer'] == 'T':
            choice = 'T'
        else:
            choice = 'F'
        option_obj = Option()
        option_obj.question_id = Question.objects.get(id = question_id)
        option_obj.option_name = kwargs['option']
        option_obj.answer = choice
        option_obj.save()
        return None

    def edit_option(self, question_id):
        options = Option.objects.filter(question_id = question_id)
        if options != None:
            option = []
            for obj in Option.objects.all():
                if obj.question_id.id == question_id:
                    option.append(obj)
            return option
        else:
            return None
    
    def edit_option_save(self, question_id, **kwargs):
        Option.objects.filter(question_id = question_id).delete()
        options = kwargs['options']
        try:
            option_imgs = kwargs['option_imgs']
        except Exception as ex:
            print ex

        for index, option in enumerate(options, start=0):
            option_obj = Option()
            option_obj.question_id = Question.objects.get(id = question_id)
            option_obj.option_name = options[index]["option_name"]
            option_obj.answer = options[index]["answer"]
            try:
                option_obj.img_option = option_imgs[index]
            except Exception as ex:
                print(ex)
            finally:
                option_obj.save()
        return None

    def __str__(self):
        return self.option_name.encode('utf8')

class Admin(models.Model):
    admin_name = models.TextField(max_length=45)

class Candidate(models.Model):
    candidate_name = models.TextField(max_length=45)