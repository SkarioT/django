from django.shortcuts import render
from cart.models import BookInCart,Cart
from books.models import Books

from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView,FormView,TemplateView

#profile
from profiles.views import ProfilesDetail,ProfilesUpdate,ProfilesList
from profiles.models import Profile
from profiles.forms import CreateProfileFormModel

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

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

class CustomersList(ProfilesList):
    template_name='s_admin/list.html'

class CustomersUpdate(ProfilesUpdate):
    template_name='s_admin/update.html'
    def get_success_url(self):
        return reverse_lazy('s-admin:customers')

class CustomersDetail(ProfilesDetail):
    template_name='s_admin/detail.html'



