import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    """
     Форма LoginUserForm для авторизации пользователей
    """
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        # get_user_model - возвращает текущую модель пользователя
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    """
    Форма RegisterUserForm для регистрации новых пользователей
    """
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        # Метки для полей - labels
        labels = {
            'email': 'E-mail',
            'first_name': "Имя",
            'last_name': "Фамилия",
        }
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        """
        Функция clean_email проверяет email на уникальность
        """
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует")
        return email

class ProfileUserForm(forms.ModelForm):
    """
    Класс ProfileUserForm
    """
    # disabled нельзя редактировать
    username = forms.CharField(disabled=True, label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(disabled=True, label="E-mail", widget=forms.TextInput(attrs={'class': 'form-control'}))

    # this_year текущий год
    this_year = datetime.date.today().year
    date_birth = forms.DateField(label="Дата рождения", widget=forms.SelectDateWidget(attrs={'class': 'form-control'}, years=tuple(range(this_year-100, this_year-5))))
    class Meta:
        model = get_user_model()
        # Поля отображаемые
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']

        # Метки для полей - labels
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        # Виджеты для полей
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
