# """Examination URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.10/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.conf.urls import url, include
#     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# """
from django.conf.urls import url
from django.conf import settings
from test_management import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^test/', views.test_list, name='test'),
    url(r'^test-management/add_test/', views.add_test, name='add_test'),
    url(r'^test-management/edit_test/', views.edit_test, name='edit_test'),
    url(r'^test-management/delete_test/', views.delete_test, name='delete_test'),
    url(r'^$', views.question_list, name='question'),
    url(r'^test-management/add_question/', views.add_question, name='add_question'),
    url(r'^test-management/edit_question/', views.edit_question, name='edit_question'),
    url(r'^test-management/delete_question/', views.delete_question, name='delete_question'),
    url(r'^test-management/import_question/', views.import_question, name='import_question'),
    url(r'^get_question_lists/$', views.get_question_lists, name='get_question_lists'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

