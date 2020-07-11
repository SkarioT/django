from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView,TemplateView
from cart.models import BookInCart,Cart
from books.models import Books
from profiles.models import Profile
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class S_Admin(LoginRequiredMixin,TemplateView):
    models=Books
    template_name='s_admin/index.html'

    def get_context_data(self, **kwargs):
        #подкидуываю в контектс для каждого обработчика в контект Profile user pk
        c= super().get_context_data(**kwargs)
        try:
            user=self.request.user
            prof_user=Profile.objects.get(username=user)
            print(user)
            print('prof_user.pk',prof_user.pk)
            c['prof_user']=prof_user.pk
        except Profile.DoesNotExist:
            prof_user=None
        return c

