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
from books.views import BooksCreate,BooksDetail,BooksUpdate,BooksDelete,BooksList
from home_page.views import Home_page
from django.conf import settings
from django.conf.urls.static import static
from books.auth_view import Mylogin,Mylogout,MyPasswordChange
from profiles import urls
from order import urls
from cart import urls
# from phones import 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home_page.as_view(),name='home_page'),
    path('catalogs/',include('test_hello_word.urls', namespace="CRUD_genre")),
    path('books/',include('books.urls', namespace="CRUDL_books")),
    path('login/',Mylogin.as_view(), name='login'),
    path('logout/',Mylogout.as_view(), name='logout'),
    path('change-password/',MyPasswordChange.as_view(), name='change-password'),
    path('profiles/',include('profiles.urls', namespace="CRUDL_profiles")),
    path('cart/',include('cart.urls', namespace="cart")),
    path('s-admin/',include('s_admin.urls', namespace="s-admin")),
    path('order/',include('order.urls', namespace="order"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#конструкция +static  специально для режими разработке, в проде эту строку нужно удалить