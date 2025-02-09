from django.core.exceptions import ValidationError, ObjectDoesNotExist
from reminder_app.forms import AuthorizationForm
from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
import secrets
from reminder_app.models import User

class AuthorizationPage(View):
    def get(self, request):
        form = AuthorizationForm()
        return render(request, 'guest/authorization.html', {'title': 'Авторизация',
                                                            'header': 'Пожалуйста, заполните все обязательные поля',
                                                            "form": form})

    def post(self, request):
        form = AuthorizationForm(request.POST)
        if form.is_valid():
            """
            Валидация формы -> получение email существующего пользователя -> сохранение формы -> создание токена 
            для определения пользователя на следующих страницах -> запись пары "токен: айди" в redis -> 
            redirect на главную страницу для авторизованных 
            пользователей
            """
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # валидация полей формы
            if not User.objects.filter(email=email):
                raise ObjectDoesNotExist('Пользователя с таким email не существует')
            elif not User.objects.filter(email=email, password=password):
                raise ValidationError('Пароль не подходит')
            # --- --- --- ---

            token = secrets.token_urlsafe(nbytes=32)
            cache.set(token, User.objects.get(email=email).id, timeout=300)
            return redirect(f'/homeauthed/{token}')
        return render(request, 'guest/registration.html', {'title': 'Авторизация',
                                                           'header': 'Пожалуйста, заполните все обязательные поля',
                                                           "form": form})
