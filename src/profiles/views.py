from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from . import models
from django.urls import reverse,reverse_lazy
#модели
from .models import Profile
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
class ProfilesCreate(CreateView):
    #куда сохронять
    model=User
    fields=('username','password','first_name','last_name','email')
    #какую форму для сохронения данных используем
    # form_class=CreateGenreFormModel
    # fields=('user','image')
    #в какой шаблон отрисовывать
    template_name='profiles/create.html'
    # success_url =reverse_lazy('CRUD_genre:list')
    def get_success_url(self):
        #return f"/detail/{self.object.pk}"
        return reverse_lazy('CRUDL_profiles:detail', kwargs={'pk':self.object.pk})


class ProfilesDetail(DetailView):
    model= Profile
    template_name='profiles/detail.html'

class ProfilesUpdate(UpdateView):
    #редактирую не профайл а дефэолдную таблицу User
    model=Profile
    fields=('user','image')
    # model= User
    # fields=('username','first_name','last_name','email','groups','is_staff','is_active','is_superuser','last_login','date_joined')
    template_name='profiles/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_profiles:detail', kwargs={'pk':self.object.pk})


class ProfilesDelete(DeleteView):
    pass

class ProfilesList(ListView):
    model=Profile
    template_name='profiles/list.html'

