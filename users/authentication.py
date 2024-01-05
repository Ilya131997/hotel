from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    """
    Класс EmailAuthBackend для аутентификации пользователя по Email
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Функция authenticate для аутентификации пользователя по Email
        """

        # user_model ссылка на текущую модель пользователя
        user_model = get_user_model()

        try:
            # Получаем пользователя по email
            user = user_model.objects.get(email=username)
            # Проверка на совпадение по паролю
            if user.check_password(password):
                # При удачной проверка возвращаем обьект пользователя
                return user
            return None
        # Исключения DoesNotExist(если не нашли нужную запись), MultipleObjectsReturned(если нашли несколько записей по email)
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        """
        Фукнция get_user
        По user_id возврат user или None
        После того как пройдена аутентификация по email, отображается пользователь
        """
        # user_model ссылка на текущую модель пользователя
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None