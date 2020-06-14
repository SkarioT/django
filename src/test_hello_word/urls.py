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
app_name="CRUD_genre"
from . import views

urlpatterns = [
    path('create/', views.Genre_Create.as_view(),name='create'),
    path('update/<int:pk>', views.Genre_Update.as_view(),name='update'),
    path('list/', views.Genre_List.as_view(),name='list'),
    path('delete/<int:pk>', views.Genre_Delete.as_view(),name='delete'),
    path('detail/<int:pk>', views.Genre_DetaleView.as_view(),name='detail')


]
