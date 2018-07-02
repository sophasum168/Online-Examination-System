# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Test, Question, Option

# Register your models here.
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)