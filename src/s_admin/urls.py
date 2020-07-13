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

from django.urls import path
app_name="s-admin"
from . import views

urlpatterns = [
    path('', views.S_Admin.as_view(),name='index'),
    path('customers', views.CustomersList.as_view(),name='customers'),
    path('customers/update/<int:pk>', views.CustomersUpdate.as_view(),name='update'),
    path('customers/detail/<int:pk>', views.CustomersDetail.as_view(),name='detail'),

    path('books', views.SAdminBooksList.as_view(),name='books'),
    path('books/create', views.SAdminBooksCreate.as_view(),name='books_create'),
    path('books/update/<int:pk>', views.SAdminBooksUpdate.as_view(),name='books_update'),
    path('books/detail/<int:pk>', views.SAdminBooksDetail.as_view(),name='books_detail'),
    path('books/delete/<int:pk>', views.SAdminBooksDelete.as_view(),name='books_delete'),

    path('genre', views.SAdminGenreList.as_view(),name='genre'),
    path('genre/create', views.SAdminGenreCreate.as_view(),name='genre_create'),
    path('genre/update/<int:pk>', views.SAdminGenreUpdate.as_view(),name='genre_update'),
    path('genre/detail/<int:pk>', views.SAdminGenreDetail.as_view(),name='genre_detail'),
    path('genre/delete/<int:pk>', views.SAdminGenreDelete.as_view(),name='genre_delete'),
    
    path('author', views.SAdminAuthorList.as_view(),name='author'),
    path('author/create', views.SAdminAuthorCreate.as_view(),name='author_create'),
    path('author/update/<int:pk>', views.SAdminAuthorUpdate.as_view(),name='author_update'),
    path('author/detail/<int:pk>', views.SAdminAuthorDetail.as_view(),name='author_detail'),
    path('author/delete/<int:pk>', views.SAdminAuthorDelete.as_view(),name='author_delete'),

    path('cart', views.SAdminCartList.as_view(),name='cart'),
    path('cart/update/<int:pk>', views.SAdminCartUpdate.as_view(),name='cart_update'),
    path('cart/detail/<int:pk>', views.SAdminCartDetail.as_view(),name='cart_detail'),
    path('cart/delete/<int:pk>', views.SAdminCartDelete.as_view(),name='cart_delete'),
]
