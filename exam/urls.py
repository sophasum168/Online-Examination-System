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
from register.views import (register,upload_file,candidate)
from django.conf import settings
from django.conf.urls.static import static
from candidate.views import cour

urlpatterns = [

	# url(r'^$', views.HomePageView.as_view(), name='home'),
	# url(r'^', views.AboutPageView.as_view(), name='about'),
	# url(r'^$', views.index, name='index'),
    # url(r'^$', views.hive_names, name='hive_names'),
    #url(r'^login/$',contrib.auth_views.login, name='login'),
    # url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', admin.site.urls),
    url(r'^register',register,name="register"),
    url(r'^upload/', upload_file, name="upload"),
    url(r'^', candidate, name="candidate"),
    url(r'^cour/', cour, name="cour"),
    # url(r'^',include('example.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
