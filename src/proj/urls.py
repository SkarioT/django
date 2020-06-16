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
from django.urls import path , include
from test_hello_word.views import test_form,test_pk,test_created,test,Test_B_V,Genre_Create,Genre_Update,Genre_List,Genre_Delete,Genre_DetaleView
from test_hello_word.views import test
# from phones import 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test,name='main_page'),
    # path('create/', Genre_Create.as_view()),
    # path('update/<int:pk>', Genre_Update.as_view()),
    # path('list/', Genre_List.as_view()),
    # path('delete/<int:pk>', Genre_Delete.as_view()),
    # path('detail/<int:pk>', Genre_DetaleView.as_view())
    path('catalogs/',include('test_hello_word.urls', namespace="CRUD_genre"))
]
