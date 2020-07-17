from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from books.models import Books
import requests
from django.urls import reverse,reverse_lazy
from books.models import Books,Binging,Author,Genre,Series,Publisher
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class Home_page(ListView):
    model=Books
    template_name='home_page/home_page.html'
    paginate_by=5
    
    def get_context_data(self, **kwargs):
        book_pk=self.request.GET.get('book_pk')
        print("book_pk:",book_pk)
        c= super().get_context_data(**kwargs)
        c['book_pk']=book_pk
         #подкидуываю в контектс для каждого обработчика в контект Profile user pk
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print(prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

# Create your views here.
