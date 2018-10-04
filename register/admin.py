# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *



class CandidateProfile(admin.ModelAdmin):
	list_filter= ('created_at','firstname','email','sname','address')
	list_display=('created_at','email','firstname','card_id','student_profile','lastname','phonenumber','birthday','sname','address','city','country')
	search_fields=('firstname','email','lastname')
	
	def get_queryset(self, request):
		queryset=super(CandidateProfile, self).get_queryset(request)
		queryset=queryset.order_by('created_at')
		return queryset

# class CandiateID(admin.ModelAdmin):
# 	# list_filter= ('created_at','firstname','email','sname','address')
# 	list_display=('card_id','student_profile')
		
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
# admin.site.register(CandiateImage, CandiateID)
admin.site.register(CandidateAnswer)