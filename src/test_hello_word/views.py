from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic.base import TemplateView
from .forms import CreateGenreForm,CreateGenreFormModel
from django.views.generic import CreateView,UpdateView,DeleteView,ListView

#from pip._vendor import requests
import requests
from .models import Genre

def test(request):
    context={}
    return render(request, template_name="test_hello_word/index.html", context={})


def test_created(request):
    if request.method=='GET':
        pass
    else:
    
        name=request.POST.get('name')
        description=request.POST.get('description')

        print(name,description)
        obj=Genre(name=name,description=description)
        obj.save()
    return render(request, template_name="test_hello_word/index_created.html", context={})

def test_pk(request,pk):
    print(request.method)
    if request.method=='GET':
        obj=Genre.objects.get(pk=pk)
        context={'name': obj.name, 'description':obj.description,'created': obj.created}
    if request.method=='POST':
        post_data=request.POST
        name=request.POST.get('name')
        description=request.POST.get('description')
        # print(post_data,pk,name,description)
        cdt=datetime.datetime.now()
        obj=Genre.objects.filter(pk=pk).update(name=name,description=description,created=cdt)
        obj=Genre.objects.get(pk=pk)
        context={'name': obj.name, 'description':obj.description,'created': obj.created}
    return render(request, template_name="test_hello_word/index_pk.html", context=context)

def test_form(request,pk=''):
    if pk=='':
        form=CreateGenreForm()
        form2=CreateGenreFormModel()
        context={'form': form,'form2': form2}
        return render(request, template_name="test_hello_word/index_form.html", context=context)
    obj=Genre.objects.get(pk=pk)
    form=CreateGenreForm({"name":obj.name,'description':obj.description})
    form2=CreateGenreFormModel({"name":obj.name,'description':obj.description})
    context={'form': form,'form2': form2}
    return render(request, template_name="test_hello_word/index_form.html", context=context)

class Test_B_V(TemplateView):
    template_name='test_hello_word/index_form_b_v.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['rate']=self.get_rate()
        return context
    def get_rate(self):
        return 2.999

class Genre_Create(CreateView):
    #куда сохронять
    model= Genre
    #какую форму для сохронения данных используем
    form_class=CreateGenreFormModel
    #в какой шаблон отрисовывать
    template_name='test_hello_word/create.html'
    success_url ='/list/'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['rate']=123
        return context
class Genre_Update(UpdateView):
    #куда сохронять
    model= Genre
    #какую форму для сохронения данных используем
    form_class=CreateGenreFormModel
    #в какой шаблон отрисовывать
    template_name='test_hello_word/update.html'
    success_url ='/list/'

    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['rate']=123
    #     return context
class Genre_List(ListView):

    model = Genre
    template_name='test_hello_word/list.html'
    # paginate_by = 100  # if pagination is desired
    # queryset= Genre.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] =datetime.datetime.now()
    #     return context
class Genre_Delete(DeleteView):
    model = Genre
    template_name='test_hello_word/delete.html'
    success_url ='/list/'