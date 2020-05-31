from django.shortcuts import render
from django.http import HttpResponse
from pip._vendor import requests


# Create your views here.
def test(request):
    eth_acc='0x5fF531736002B2a9Cd4dAb79A55Ab504F1dC3195'
    r=requests.get('https://api.nanopool.org/v1/eth/user/{}'.format(eth_acc))
    rez=r.json()
    balance=rez.get('data').get('balance')
    key=rez.get('data')
    values=rez.get('data').values()
    context={'balance' : balance, 'key': key,'values':values}
    #context=r
    return render(request, template_name="test_hello_word/index.html", context=context)
