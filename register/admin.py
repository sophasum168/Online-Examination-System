# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class CandidateProfile(admin.ModelAdmin):
	list_filter= ('firstname','email','sname')
	list_display=('created_at','email','firstname','lastname','phonenumber','birthday','sname','address','city','country','file','image')
	
	def get_queryset(self, request):
		queryset=super(CandidateProfile, self).get_queryset(request)
		queryset=queryset.order_by('created_at')
		return queryset
		
# class ProfileImagesInline(admin.TabularInline):
#     model = Register
#     extra = 3

# class ProfileAdmin(admin.ModelAdmin):
#     inlines = [ ProfileImagesInline, ]
# Register your models here.
# class RegisterAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__","timestamp","updated"]
# 	class Meta:
# 		model = Register					
admin.site.register(Register, CandidateProfile)
admin.site.register(Image)