from django.shortcuts import render
from django.http import HttpResponse
import datetime


#from pip._vendor import requests
import requests
from .models import Parser_log



#objects.count() посчите кол-во элементов в базеs
def test(request):
    # cd=datetime.datetime.now()
    # блок когда через который заливал базу
    # i=0
    # while i < 10000:
    #     create_parser_item=Parser_log(browser=Parser_log.get_word_4_possition(i,'lw'), text_log=Parser_log.get_word_4_possition(i,'all'), date_ivents=Parser_log.get_word_4_possition(i,3))
    #     i+=1
    #     create_parser_item.save()
    i=0
    cdr=datetime.datetime.now()
    while i < 10000:
        create_parser_item=Parser_log(update=cdr).update()
        i+=1
        create_parser_item.save()
    # delete=Parser_log.objects.all()
    # delete.delete()
    parser=Parser_log.objects.filter(browser__startswith='Safari')
    safari=Parser_log.objects.filter(browser__startswith='Safari').count()

    # parser11=Parser_log.objects.filter(browser__startswith='Safari')
    # firefox=Parser_log.objects.filter(browser__startswith='Safari').count()
    parser11=Parser_log.objects.filter(browser__startswith='Firefox')
    firefox=Parser_log.objects.filter(browser__startswith='Firefox').count()

    parser3=Parser_log.objects.exclude(browser__startswith='Firefox').exclude(browser__startswith='Safari')
    excludee=parser2=Parser_log.objects.exclude(browser__startswith='Firefox').exclude(browser__startswith='Safari').count()
    #parser=Parser_log.objects.filter(browser='Safari/537.36').all()
    # parser=Parser_log.objects.get(browser='Safari/537.36')
    context ={'parser' : parser,'parser2' : parser11,'safari' : safari,'firefox': firefox, "parser3" : parser3, "excludee" : excludee}
    # context ={'browser' : Parser_log.get_word_4_possition(1,'lw'),'ddata':Parser_log.get_word_4_possition(1,3),'all_text':Parser_log.get_word_4_possition(1,'all')}
    return render(request, template_name="test_hello_word/index.html", context=context)

#различные тесты, пробы и ошибки
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


