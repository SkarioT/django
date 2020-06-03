import datetime
import pytz
import calendar
import os


cdt = datetime.datetime.now().date()
str_cdt=cdt.strftime("%d/%B")
print(str_cdt)
#заношу в виде строки
date_to_str=str(cdt)
#меняю в строке  - на _
clear_str=date_to_str.replace('-',' ')
#разбиваю на отдельные слова
slice_str=clear_str.split()
#cоздаю новую дату +2 дня к ней
creat_date=datetime.datetime(int(slice_str[0]),int(slice_str[1]),int(slice_str[2])+2)
print("созданная дата 17.00 : ",creat_date)

# через dimedelta
td=datetime.timedelta(minutes=3)
print("отнимаем от созаднной даты 3 минуты(td) : ",creat_date-td)

#из строки делаем время
strptime=datetime.datetime.strptime('1803191327','%d%m%y%H%M')
print("из строки далем время",strptime)


# import sys
# print("sys.path : \n",sys.path)
# print("\n fp_date.__file__ : \n",pytz.__file__)


# print(fp_date.count_lines())
# print(fp_date.last_word_on_line(6666))
# print(fp_date.def_counter(fp_date.get_ip(1)))
print('_'*30)

format_date_on_log='17/May/2015:10:05:00'
#cоздаю дату из строки введенных данных
cdt=datetime.datetime(2020,5,5)
print('созданная дата из цфр ',cdt)
format_calculate_date='0:00:16.603720'

print("format_date_on_log=",format_date_on_log)
time_obj=datetime.datetime.strptime(format_date_on_log,'%d/%B/%Y:%H:%M:%S')
print("time_obj",time_obj)

tz_minsk = pytz.timezone("Europe/Minsk")
tz_utc   = pytz.timezone('UTC')
ct_minsk=datetime.datetime.now()
d_minsk=tz_minsk.localize(ct_minsk)
utc_minsk=d_minsk.astimezone(tz_utc)
print('_'*30)
print(utc_minsk)
print(d_minsk)








#текущее время в UTC
# ct_utc=datetime.datetime.utcnow()
#текущенее время в +3
# ct_minsk=datetime.datetime.now()
# 
# d_minsk=tz_minsk.localize(ct_minsk)
# d_utc=tz_utc.localize(ct_utc)
# d_minsk_utc=d_utc.astimezone(tz_utc)
# print("Вывод  d_minsk в формете +3 Europe/Minsk :",d_minsk)
# print("Вывод  d_minsk в формете             UTC :",d_utc)
# print("Вывод  d_minsk в формете     d_minsk_utc :",d_minsk_utc)
os.system('cls' if os.name=='nt' else 'clear')