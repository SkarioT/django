from django.db import models
import datetime
# # Create your models here.
# class Genre(models.Model):
#     #id/pk
#     name = models.CharField(
#         verbose_name ="Название Жанра",
#         max_length=100
#         ) # столбец name тип данных CharField
#     description = models.TextField(
#         verbose_name="Описание Жанра",
#         null=True,
#         blank=True
#     )
#     created=models.DateField(
#         verbose_name="Дата создания",
#         auto_now=True,
#         auto_now_add=False
#     )
#     update=models.DateField(
#         verbose_name="Дата обновления",
#         auto_now=False,
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.name
    

# class Book(models.Model):
#     name = models.CharField(
#         verbose_name ="Название книги",
#         max_length=200
#     )
#     description = models.TextField(
#         verbose_name="Описание книги",
#         null=True,
#         blank=True
#     )
#     genre=models.ForeignKey(
#         Genre,
#         on_delete=models.PROTECT,
#         verbose_name="Жанр Книги"
#     )
#     created=models.DateField(
#         verbose_name="Дата создания",
#         auto_now=True,
#         auto_now_add=False
#     )
#     update=models.DateField(
#         verbose_name="Дата обновления",
#         auto_now=False,
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.name    
#      # столбец name тип данных CharField

class Parser_log(models.Model):
    browser = models.CharField(
        verbose_name ="Название Браузера",
        max_length=200,
        null=True,
        blank=True
    )
    text_log = models.TextField(
        verbose_name="Описание книги",
        null=True,
        blank=True
    )
    date_ivents=models.DateTimeField(
        verbose_name="Дата события",
        auto_now=False,
        auto_now_add=False
    )
    created=models.DateField(
        verbose_name="Дата создания",
        auto_now=True,
        auto_now_add=False
    )
    update=models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.browser   
     # столбец name тип данных CharField
    
    
# with open('1.txt','r') as fp:
#     myfile_lines=fp.readlines()
#     fp.seek(0)
#     myfile_read=fp.read()


#функция полсчтёта кол-во строк
    def count_lines():
        with open('1.txt','r') as fp:
            myfile_lines=fp.readlines()
            fp.seek(0)
            myfile_read=fp.read()
        coun_str_in_file=(myfile_read.count('\n'))+1 #+1 т.к. в текущем файле последняя строка не имеет перенос
        return coun_str_in_file


#фукция для получения WORD из N строки. 
    def get_word_4_possition(number_line,number_word=0):
        with open('1.txt','r') as fp:
            myfile_lines=fp.readlines()
            fp.seek(0)
            myfile_read=fp.read()
        #берём n строку из листа и заносим в отдельную строку
        list_to_str=myfile_lines[int(number_line)]
        #полученную строку разделяю на отдельный слова
        split_str=list_to_str.split()
        #для последнего слова  получаю ID его позиции
        len_str=len(split_str)-1
        if number_word=='all':
            word_4_possition=split_str
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
        # else:
        #     word_4_possition=split_str[number_word]
        return word_4_possition

    def def_rez():
        with open('1.txt','r') as fp:
            myfile_lines=fp.readlines()
            fp.seek(0)
            myfile_read=fp.read()
        i=0
        while i < 10 :
            print(get_word_4_possition(i,3),get_word_4_possition(i,'lw'),myfile_lines[i])
            i+=1

