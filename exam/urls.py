"""Examination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib import photo_upload
from django.views.generic import TemplateView
from register.views import *
from livertc.views import *
from test_management import views
from register.views import *
from Landingpage.views import (landingpage)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from register import views
# from capture.views import (PersonaCreateView, SaveImage, template)
from test_management import urls as test_management_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$',login_view,name="login"),
    # sokmeng
    url(r'^logout/$',logout_view,name="logout"),
    # 
    url(r'^register/$',register,name="register"),
    url(r'^upload/', upload_file, name="upload"),
    url(r'^livertc/', livertc, name="livertc"),
    url(r'^save_image/(?P<cedula>\d+)/$',view=SaveImage.as_view(),name='salvar_imagen'),
    url(r'^candidate/', candidate, name="candidate"),
    # url(r'^template/', template, name="template"),
    url(r'^model_form_upload/$', model_form_upload, name="model_form_upload"),
    # url(r'^landingpage/', landingpage, name="landingpage"),
    url(r'^edit_candidate/',edit_candidate, name='edit_candidate'),
    url(r'^delete_candidate/',delete_candidate, name='delete_candidate'),
    url(r'^video_upload/',video_upload, name='video_upload'),
    url(r'^submit_answer/',submit_answer, name='submit_answer'),
    url(r'^', include(test_management_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
