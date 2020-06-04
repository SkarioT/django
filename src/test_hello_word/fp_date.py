# парсим файл логов:
# 1) подсчёт кол-во строк 
# 2) подсчёт уникальных IP
# 3) подсчёт браузеров(cколько запросов от Safari и от Firefox)
# 4) разбивка по датам:
# 4.1) кол-во уникальных ип в дату(дней 3)
# 4.2) cколько браузеров в каждый день
import datetime
import pytz
import calendar
import os

with open('1.txt','r') as fp:
    myfile_lines=fp.readlines()
    fp.seek(0)
    myfile_read=fp.read()

form_ip=r''
#функция полсчтёта кол-во строк
def count_lines():
    coun_str_in_file=(myfile_read.count('\n'))+1 #+1 т.к. в текущем файле последняя строка не имеет перенос
    return coun_str_in_file


#фукция для получения WORD из N строки. 
def get_word_4_possition(number_line,number_word=0):
    #берём n строку из листа и заносим в отдельную строку
    list_to_str=myfile_lines[int(number_line)]
    #полученную строку разделяю на отдельный слова
    split_str=list_to_str.split()
    #для последнего слова  получаю ID его позиции
    len_str=len(split_str)-1
    if number_word==0:
        word_4_possition=split_str[number_word]
    if number_word==3: 
        #отдельный блок для перевода строки в дату
        rez=split_str[number_word]
        clear_str=rez.replace('[','')
        time_obj=datetime.datetime.strptime(clear_str,'%d/%B/%Y:%H:%M:%S')
        return time_obj
    if number_word=="lw":
        number_word=len_str
        rez=split_str[number_word]
        word_4_possition=rez.replace('\"','')
    else:
        word_4_possition=split_str[number_word]
    return word_4_possition
i=0
while i <10 :
    print(get_word_4_possition(i,3),get_word_4_possition(i,'lw'),myfile_lines[i])
    i+=1


#функция возвращает лист состоящий из слов по позиции
#если на вход подать только слово(без второго параметра) - то вернеться, по умолчанию,список состоящий из последних слов ,т.е. по браузеров
#если получаем на 2 позицию int, то этот int == поцизии слова в строке и вереться спискок состоящий из этих слов
def def_word_list(name_word="Safari",word_possition="lw"):
    rez_list_browser_list=list()
    i=0
    while i < count_lines():
        #проверка на КОНКРЕТНЫЙ браузер
        if name_word ==0:
            #print("зашли в первый иф")
            rez_list_browser_list.append(get_word_4_possition(i,word_possition))
        elif word_possition==3:
            #print("зашли 2 иф")
            #get_word_4_possition 4 2015-05-17 10:05:43)
            #отдельный блок для перевода из даты в строку для поиска минимальной
            non_str_data=get_word_4_possition(i,3)
            str_datatime=non_str_data.strftime("%d.%m.%Y %H:%M:%S") # %H:%M
            #type_datatime=rez_list_browser_list.append(str_datatime)
            #if str_datatime.startswith(str(name_word)):
            rez_list_browser_list.append(str_datatime)
        elif word_possition=="lw":
        #get_word_4_possition(i,word_possition).startswith(str(name_word)):
            rez_list_browser_list.append(get_word_4_possition(i,word_possition))
        i+=1
    return rez_list_browser_list

def find_date(d=17):
    rez_list_browser_list=list()
    i=0
    while i < count_lines():
        type_datatime=get_word_4_possition(i,3)
    return 

#функция возвращает уникальные значения( как для IP(первых слов) так и для браузеров(последних слов))
def uniq(function_name):
    uniq=[]
    for line in function_name:
        if line not in uniq:
            uniq.append(line)
    return uniq

# 1 cпособ подсчтета браузеров(конечных слов), используя counter 
def def_counter (name,possition):
    from collections import Counter
    cnt = Counter()
    for word in def_word_list(name,possition):
        cnt[word] += 1
    return dict(cnt)

def def_counter2 (a=None):
    from collections import Counter
    cnt = Counter()
    while i<count_lines():
        for word in get_word_4_possition(i,'lw'):
            cnt[word] += 1
        i+=1
    return dict(cnt)

print('def_counter2',def_counter2)
# def ctc(): #печает время в UTC и +3 не используя .utcnow()
#     tz_minsk = pytz.timezone("Europe/Minsk")
#     tz_utc   = pytz.timezone('UTC')
#     ct_minsk=datetime.datetime.now()
#     d_minsk=tz_minsk.localize(ct_minsk)
#     utc_minsk=d_minsk.astimezone(tz_utc)
#     print(utc_minsk)
#     print(d_minsk)



# print("Текущее время в UTC/+3:")
# ctc()

# #функцция вычислят минимальную дату и максимальную дату найденную в логе и возвращает значение этих дат
# def get_min_max_date():
#     data_=def_word_list(0,3)
#     global min_data
#     global max_data
#     min_data=min(data_)
#     max_data=max(data_)
#     min_time_str=datetime.datetime.strftime(min_data,'%d %m %Y %H %M %S').split()
#     max_time_str=datetime.datetime.strftime(max_data,'%d %m %Y %H %M %S').split()
#     min_day=min_time_str[0]
#     max_day=max_time_str[0]
#     return min_day,max_day


# date_start=datetime.datetime.now()
# print("Вычисление минимальной и максимальной даты для поиска... ")
# #вызываем функцию для вычисления минимальной и максимальной доступной даты дату
# #заношу в переменную real_day - результат функции(т.е. минимальную и максимальную возможную дату)
# real_day=get_min_max_date()
# date_stop_calculate=datetime.datetime.now()

# print("Вычисление произведено за : ",date_stop_calculate-date_start,"cекунд(ы)")


# #print("get_word_4_possition 4",(get_word_4_possition(1,3)))
# # type_datatime=get_word_4_possition(1,3)
# # str_datatime=type_datatime.strftime("%d%m%Y")
# # 
# # print("get_word_4_possition 4  STR",str_datatime)


# while True:
#     menu=input("Выберите пунк меню для работы:\n1)Узнать кол-во всех строк\n2)Узнать кол-во ВСЕХ IP\n3)Меню поиска по параметру(IP|Дата|Браузер)\n Ваш выбор?:")
#     if menu=='1':      
#         print("кол-во строк : ",count_lines())
#     if menu=='2':
#         print("кол-во ВСЕХ IP: ",len(def_word_list(0,0)))
#     if menu=='3':
#         print('_'*20,"\nВыбран поиск по параметру")
#         while True:
#             input_menu_3=input("Введите что будем искать:\n1)Поиск по IP\n2)Поиск по дате\n3)Поиск браузеру\n4)Выход в предыдущее меню\n Ваш выбор?:")
#             if input_menu_3=='1':
#                 print("Выбран поиск по IP")
#                 inptut_ip=input("Введите IP для поиска(можно частично): ")
#                 print("Кол-во запросов с IP {} :".format(inptut_ip),len(def_word_list(inptut_ip,0)))
#                 print("Cписок IP {} :".format(inptut_ip),(def_word_list(inptut_ip,0)))
#                 print("Cписок уникальных IP из {} :".format(inptut_ip),uniq(def_word_list(inptut_ip,0)))
#                 print("Кол-во запросов от IP из {} :".format(inptut_ip),(def_counter(inptut_ip,0)))
#             if input_menu_3=='2':
#                 print("Выбран поиск по Дате")

#                 inptut_day=input("Введите дату для поиска(конкретный день, на пример число 17)\nМинимальная дата {} максимальная дата {}\nВаш выбор?: ".format(min_data,max_data))
#                 #проверка на корректность ввода даты
#                 while (int(real_day[0])> int(inptut_day)) or (int(real_day[1])< int(inptut_day)):
#                     inptut_day=input("Не корркетный ввод. Дата не должна быть меньше и/или больше  минимальной/максимальной даты\nВведите дату для поиска(можно частично,на пример только день)\nМинимальная дата {} максимальная дата {}\nВаш выбор?: ".format(min_data,max_data))
#                 print("Кол-во запросов  в дату {} :".format(inptut_day),len(def_word_list(inptut_day,3)))
                
#                 #print("Список запросов  в дату {} с указанием времени:".format(inptut_day),(def_word_list(inptut_day,3)))
#                 print("Кол-во уникальных запросов за {} число с указанием времени(ЧЧ:ММ:СС) - {} ,перечень этих запросов: ".format(inptut_day,(len(uniq(def_word_list(inptut_day,3))))),(uniq(def_word_list(inptut_day,3))))     
#                 print("\n"*3,"Кол-во запросов за  {} число с указанием их кол-ва в конкретную секунду:".format(inptut_day),(def_counter(inptut_day,3)))
#             if input_menu_3=='3':
#                 print("Выбран поиск по Браузеру")
#                 inptut_ip=input("Введите название браузера для поиска(можно частично): ")
#                 print("Кол-во запросов c браузером {} :".format(inptut_ip),len(def_word_list(inptut_ip,'lw')))
#                 print("Cписок Браузеров {} и их версии :".format(inptut_ip),(def_word_list(inptut_ip,'lw')))
#                 dub_input=input("Убрать дублирующие записи и подситать кол-во уникальны?\nВведите д - для выполениня опарации или введите любой другой символ для пропуска данного меню:")
#                 if dub_input=='д':
#                     print("Спискок браузеров и их версии без дубликавов")
#                     print("Cписок Браузеров {},их версии и кол-во:".format(inptut_ip),def_counter(inptut_ip,'lw'))
#             if input_menu_3=='4':
#                 break


