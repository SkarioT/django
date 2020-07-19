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
        nbrb = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
        course = nbrb.json()
        rate = {}
        for c in course:
            if c.get('Cur_Abbreviation') == 'USD':
                rate['USD'] = c.get('Cur_OfficialRate') * c.get('Cur_Scale')
            elif c.get('Cur_Abbreviation') == 'EUR':
                rate['EUR'] = c.get('Cur_OfficialRate') * c.get('Cur_Scale')
            elif c.get('Cur_Abbreviation') == 'RUB':
                rate['RUB'] = c.get('Cur_OfficialRate') * c.get('Cur_Scale')
        context = super().get_context_data(**kwargs)
        context = {'USD': rate.get('USD'), 'EUR': rate.get('EUR'), 'RUB': rate.get('RUB'), 'rate': rate}
        return context