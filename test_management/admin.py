# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test, Subject, Topic, Question, Option

# Register your models here.
admin.site.register(Test)
admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Option)