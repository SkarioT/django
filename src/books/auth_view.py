from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Mylogin(LoginView):
    template_name='auth/login.html'


class Mylogout(LogoutView):
    pass

class MyPasswordChange(LoginRequiredMixin,PasswordChangeView):
    template_name='auth/password-change.html'

    def get_success_url(self):
        return reverse_lazy('home_page')