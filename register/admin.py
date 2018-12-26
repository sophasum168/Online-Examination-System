# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# # class CandidateProfile(admin.ModelAdmin):
# 	list_filter= ('created_at','firstname','email','sname','address')
# 	list_display=('created_at','email','firstname','card_id','student_profile','lastname','phonenumber','birthday','sname','address','city','country')
# 	search_fields=('firstname','email','lastname')
	
# 	def get_queryset(self, request):
# 		queryset=super(CandidateProfile, self).get_queryset(request)
# 		queryset=queryset.order_by('created_at')
# 		return queryset

@admin.register(Register)
class PersonAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Image)
# admin.site.register(PersonAdmin)
# admin.site.register(CandiateImage, CandiateID)
admin.site.register(CandidateAnswer)