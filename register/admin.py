# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Register
from .models import Image

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
					
admin.site.register(Register) 
admin.site.register(Image)