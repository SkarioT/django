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
    


# Create your views here.
