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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class ProfilesCreate(SuccessMessageMixin,FormView):
    form_class=CreateProfileFormModel
    template_name='profiles/create.html'
    success_message=''
    obj_profile=''
    def get_success_url(self):
        return reverse_lazy('login')#, kwargs={'pk':self.object.pk})

    def form_valid(self, form):
        formdata=form.cleaned_data
        #блок для User
        username=formdata['username']
        password=formdata['password']
        email=formdata['email']
        #блок для Profiles
        phone=formdata['phone']
        first_name=formdata['first_name']
        last_name=formdata['last_name']
        address_1=formdata['address_1']
        address_2=formdata['address_2']
        city=formdata['city']
        county=formdata['county']
        zip_code=formdata['zip_code']

        user=self.request.user
        print(user)

        print("username:",username,'\npassword:',password)
        obj_user=User(username=username,email=email)
        obj_user.set_password(password)
        obj_user.save()
        #получаю id созданого объекта в USER
        obj_user_id=obj_user.id
        obj_user_user=obj_user.username
        # он равен user созданого PROFILES
        print(obj_user_id,obj_user_user)

        obj_profile=Profile.objects.filter(user=obj_user_id).update(
        username=username,
        email=email,
        phone=phone,
        first_name=first_name,
        last_name=last_name,
        address_1=address_1,
        address_2=address_2,
        city=city,
        county=county,
        zip_code=zip_code
        )
        success_message = self.get_success_message(form.cleaned_data)
        # obj, created = Profile.objects.get_or_create(
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        usern=cleaned_data['username']
        pswd=cleaned_data['password']
        return f"Profile {usern} was created. Your password {pswd}"







class ProfilesDetail(LoginRequiredMixin,DetailView):
    model= Profile
    template_name='profiles/detail.html'



class ProfilesUpdate(LoginRequiredMixin,UpdateView):
    #редактирую не профайл а дефэолдную таблицу User
    model=Profile
    fields=('email','phone',
        'first_name',
        'last_name',
        'address_1',
        'address_2',
        'city',
        'county',
        'zip_code')
    # model= User
    # fields=('username','first_name','last_name','email','groups','is_staff','is_active','is_superuser','last_login','date_joined')
    template_name='profiles/update.html'
    def get_success_url(self):
        return reverse_lazy('CRUDL_profiles:detail', kwargs={'pk':self.object.pk})




class ProfilesDelete(LoginRequiredMixin,DeleteView):
    pass

class ProfilesList(LoginRequiredMixin,ListView):
    model=Profile
    template_name='profiles/list.html'



