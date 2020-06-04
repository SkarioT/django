from django.shortcuts import render
from django.http import HttpResponse
import datetime


#from pip._vendor import requests
import requests
from .models import Parser_log

#objects.count() посчите кол-во элементов в базе
def test(request):
    cd=datetime.datetime.now()
    create_parser_item=Parser_log(browser='Хром', text_log='Многобукф для хрома', date_ivents=cd)
    create_parser_item.save()

test(1)

