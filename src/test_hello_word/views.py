from django.shortcuts import render
from django.http import HttpResponse
import datetime


#from pip._vendor import requests
import requests
from .models import Parser_log



#objects.count() посчите кол-во элементов в базе
def test(request):
    # cd=datetime.datetime.now()
    # create_parser_item=Parser_log(browser='Хром', text_log='Многобукф для хрома', date_ivents=cd
    # create_parser_item.save()

    # parser=Parser_log.objects.all()
    # context ={'parser' : parser}
    context ={'browser' : Parser_log.get_word_4_possition(1,'lw'),'ddata':Parser_log.get_word_4_possition(1,3),'all_text':Parser_log.get_word_4_possition(1,'all')}
    return render(request, template_name="test_hello_word/index.html", context=context)


# Create your views here.
# def test(request):
#     eth_acc='0x5fF531736002B2a9Cd4dAb79A55Ab504F1dC3195'
#     r=requests.get('https://api.nanopool.org/v1/eth/user/{}'.format(eth_acc))
#     rez=r.json()
#     balance=rez.get('data').get('balance')
#     avgH=rez.get('data').get('avgHashrate').get('h24')
#     key=rez.get('data')
#     values=rez.get('data').values()
#     genre = Genre.objects.filter(name="Ботанство")
#     all_g = Genre.objects.all()
#     all_b = Book.objects.all()
#     #genre = Genre.objects.all()
#     context={'balance' : balance, 'key': key,'values':values,'h24': avgH,'genre': genre,'all_g' : all_g,'all_b' : all_b}
    

#     return render(request, template_name="test_hello_word/index.html", context=context)


