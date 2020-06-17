from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from . import models
from django.urls import reverse,reverse_lazy
from .models import Profile
class ProfileCreate(CreateView):
    #куда сохронять
    model=Profile
    #какую форму для сохронения данных используем
    # form_class=CreateGenreFormModel
    fields=('name','image')
    #в какой шаблон отрисовывать
    template_name='profiles/create.html'
    # success_url =reverse_lazy('CRUD_genre:list')
    def get_success_url(self):
        #return f"/detail/{self.object.pk}"
        return reverse_lazy('CRUD_profiles:detail', kwargs={'pk':self.object.pk})

class ProfileDetail(DetailView):
    model= models.Books
    template_name='profiles/detail.html'

class ProfileUpdate(UpdateView):
    pass

class ProfileDelete(DeleteView):
    pass

class ProfileList(ListView):
    pass