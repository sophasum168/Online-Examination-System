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
from django.conf.urls import url
from django.contrib import admin
# from django.contrib import photo_upload
from django.views.generic import TemplateView
from register.views import (register,upload_file,candidate,congratulation,SaveImage)
from django.conf import settings
from django.conf.urls.static import static
# from capture.views import (PersonaCreateView, SaveImage, template)
from candidate.views import (cour,index)
from test_management.views import (test_list, add_test, edit_test, delete_test,
                                    question_list, add_question, edit_question, delete_question,
                                    import_question)
                                    
urlpatterns = [
	# url(r'^$', views.HomePageView.as_view(), name='home'),
	# url(r'^', views.AboutPageView.as_view(), name='about'),
	# url(r'^$', views.index, name='index'),
    # url(r'^$', views.hive_names, name='hive_names'),
    #url(r'^login/$',contrib.auth_views.login, name='login'),
    # url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', admin.site.urls),
    url(r'^register/',register,name="register"),
    url(r'^upload/', upload_file, name="upload"),
    url(r'^save_image/(?P<cedula>\d+)/$',view=SaveImage.as_view(),name='salvar_imagen'),
    url(r'^test-management/test/', test_list, name='test'),
    url(r'^test-management/add_test/', add_test, name='add_test'),
    url(r'^test-management/edit_test/', edit_test, name='edit_test'),
    url(r'^test-management/delete_test/', delete_test, name='delete_test'),
    url(r'^test-management/question/', question_list, name='question'),
    url(r'^test-management/add_question/', add_question, name='add_question'),
    url(r'^test-management/edit_question/', edit_question, name='edit_question'),
    url(r'^test-management/delete_question/', delete_question, name='delete_question'),
    url(r'^test-management/import_question/', import_question, name='import_question'),
    url(r'^candidate/', candidate, name="candidate"),
    url(r'^cour/', cour, name="cour"),
    # url(r'^photo/', include('photo_upload.urls')),
    url(r'^index/', index, name="index"),
    # url(r'^template/', template, name="template"),
    url(r'^congratulation/', congratulation, name="congratulation"),
    # url(r'^save_image/', save_image, name="save_image"),
    # url(r'^upload_webcam/', upload_webcam, name="upload_webcam"),
    # url(r'^save_filewc/', save_filewc, name="save_filewc"),
    # url(r'^persona/', view= PersonaCreateView.as_view(), name='add_persona'),
    # url(r'^save_image/', view=SaveImage.as_view(), name='salvar_imagen'),
    # url(r'^save_image/(?P<cedula>\d+)/$', view=SaveImage.as_view(), name='salvar_imagen'),
    # url(r'^',include('example.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)