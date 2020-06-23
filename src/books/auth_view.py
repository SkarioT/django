from django.contrib.auth.views import LoginView,LogoutView



class Mylogin(LoginView):
    template_name='auth/login.html'


class Mylogout(LogoutView):
    pass