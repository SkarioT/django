"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test_hello_word.views import test_form,test_pk,test_created,test,Test_B_V,Genre_Create,Genre_Update,Genre_List


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test),
    path('test_created/', test_created),
    path('test_form/', test_form),
    path('test_form/<int:pk>', test_form),
    path('test_pk/<int:pk>', test_pk),
    path('test_b_v/', Test_B_V.as_view()),
    path('create/', Genre_Create.as_view()),
    path('update/<int:pk>', Genre_Update.as_view()),
    path('list/', Genre_List.as_view())
]
