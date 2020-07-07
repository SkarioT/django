from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from . import models
from .forms import CreateProfileFormModel
from django.urls import reverse,reverse_lazy
#модели
from .models import Profile
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class ProfilesCreate(FormView):
    form_class=CreateProfileFormModel
    template_name='profiles/create.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_profiles:list')

    def form_valid(self, form):
        formdata=self.get_form_kwargs()
        username=formdata['data']['username']
        password=formdata['data']['password']
        print("username:",username,'\npassword:',password)
        obj_user=User(username=username,password=password)
        obj_user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

# class ProfilesCreate(CreateView):
#     #куда сохронять
#     model=Profile
#     # model=Profile
#     fields=('username','password','first_name','last_name','email')

#     #какую форму для сохронения данных используем
#     # form_class=CreateGenreFormModel
#     # fields=('user','image')
#     #в какой шаблон отрисовывать
#     template_name='profiles/create.html'

#     def get_success_url(self):
#         #return f"/detail/{self.object.pk}"
#         return reverse_lazy('CRUDL_profiles:detail', kwargs={'pk':self.object.pk})


class ProfilesDetail(DetailView):
    model= Profile
    template_name='profiles/detail.html'

class ProfilesUpdate(UpdateView):
    #редактирую не профайл а дефэолдную таблицу User
    model=Profile
    fields=('user','phone','home_address')
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

