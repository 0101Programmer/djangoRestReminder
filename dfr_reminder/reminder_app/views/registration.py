from datetime import datetime

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views import View
from reminder_app.forms import RegistrationForm
from django.core.cache import cache
import secrets
from reminder_app.models import User


class RegistrationPage(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'guest/registration.html', {'title': 'Регистрация',
                                                           'header': 'Пожалуйста, заполните все обязательные поля',
                                                           "form": form})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            """
            Валидация формы -> получение email нового пользователя -> сохранение формы -> создание токена для 
            определения пользователя на следующих страницах -> запись пары "токен: айди" в redis ->
            redirect на главную страницу для авторизованных пользователей
            """
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            birthdate = str(form.cleaned_data["birthdate"])

            # валидация полей формы
            if name.isdigit():
                raise ValidationError("Имя не может состоять толчок из цифр")
            elif len(password) < 5 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                raise ValidationError("Пароль должен быть более 5-ти символов, а также содержать цифры")
            elif password != password_confirmation:
                raise ValidationError("Пароли не совпадают")
            elif User.objects.filter(email=email):
                raise ValidationError("Пользователь с таким email уже существует")
            try:
                datetime.strptime(birthdate, "%Y-%m-%d")
            except ValueError:
                raise ValidationError("Пожалуйста, введите дату рождения в следующем формате: 'ГГГГ-ММ-ДД' ")
            # --- --- --- ---

            form.save()
            token = secrets.token_urlsafe(nbytes=32)
            cache.set(token, User.objects.get(email=email).id, timeout=300)
            return redirect(f'/homeauthed/{token}')
        return render(request, 'guest/registration.html', {'title': 'Регистрация',
                                                           'header': 'Пожалуйста, заполните все обязательные поля',
                                                           "form": form})
