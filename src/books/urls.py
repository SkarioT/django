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
app_name="CRUDL_books"
from . import views

urlpatterns = [
    # path('create/', views.BooksCreate.as_view(),name='create'),
    path('detail/<int:pk>', views.BooksDetail.as_view(),name='detail'),
    # path('update/<int:pk>', views.BooksUpdate.as_view(),name='update'),
    # path('delete/<int:pk>', views.BooksDelete.as_view(),name='delete'),
    path('list/', views.BooksList.as_view(),name='list'),

    path('genre_list', views.GenreList.as_view(),name='genre_list'),
    path('genre_detail/<int:pk>', views.GenreDetail.as_view(),name='genre_detail'),

    path('author_list', views.AuthorList.as_view(),name='author_list'),
    path('autrhor_detail/<int:pk>', views.AuthorDetail.as_view(),name='author_detail'),

    path('publisher_list', views.PublisherList.as_view(),name='publisher_list'),
    path('series_list', views.SeriesList.as_view(),name='series_list'),
]
