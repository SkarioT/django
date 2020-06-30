from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView



class Mylogin(LoginView):
    template_name='auth/login.html'


class Mylogout(LogoutView):
    pass

class MyPasswordChange(PasswordChangeView):
    template_name='auth/password-change.html'