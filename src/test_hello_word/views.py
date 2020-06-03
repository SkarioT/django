from django.shortcuts import render
from django.http import HttpResponse
#from pip._vendor import requests
import requests
from .models import Parser_log

def test(request):
    return "text"

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


