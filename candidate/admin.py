# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import course
from .models import MyUsers
# Register your models here.
admin.site.register(course)
admin.site.register(MyUsers)  