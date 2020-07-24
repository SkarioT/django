from django.shortcuts import render
from datetime import datetime
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView
from books.models import Books
import requests
from .models import CourseData
from django.urls import reverse,reverse_lazy
from books.models import Books,Binging,Author,Genre,Series,Publisher
from profiles.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

class Home_page(ListView):
    model=Books
    template_name='home_page/home_page.html'
    # paginate_by=5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cd=datetime.now().date()
        dbcd=CourseData.objects.last()

        if cd==(dbcd.create):
            print("даты равны")
            context['USD']=dbcd.usd
            context['EUR']=dbcd.eur
            context['RUB']=dbcd.rub
        else:
            print("даты не равны, выполняется запрос к сайту+занесения в бд")
            nbrb = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
            course = nbrb.json()
            rate = {}
            for c in course:
                if c.get('Cur_Abbreviation') == 'USD':
                    context['USD'] = c.get('Cur_OfficialRate') 
                elif c.get('Cur_Abbreviation') == 'EUR':
                    context['EUR'] = c.get('Cur_OfficialRate')
                elif c.get('Cur_Abbreviation') == 'RUB':
                    context['RUB'] = c.get('Cur_OfficialRate') 

        cdn,created=CourseData.objects.get_or_create(
            create=cd,
            usd=context['USD'],
            eur=context['EUR'],
            rub=context['RUB'],
            defaults={
            }
            )
        if created:
            print("запрос выполнент, данные занесены в БД")
        return context

    def get_queryset(self):
        return self.model.objects.all().filter(availability=True).order_by('created')[:5]