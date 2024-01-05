from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm



class LoginUser(LoginView):
    """
    Класс LoginUser для авторизации пользователя
    """
    form_class = LoginUserForm
    template_name = 'users/login.html'


class RegisterUser(CreateView):
    """
    Класс RegisterUser для регистрации новых пользователей
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class ProfileUser(LoginRequiredMixin, UpdateView):
    """
    Класс ProfileUser для страницы пользователя
    LoginRequiredMixin - только для авторизованных пользователей
    """
    # get_user_model для получения текущуй модели пользователя
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        """
        Функция get_success_url для перенаправления на текущую страницу пользователя
        """
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """
        Функция get_object позваоляет отбирать ту запись которая будет отображаться и редактироваться
        """
        return self.request.user
