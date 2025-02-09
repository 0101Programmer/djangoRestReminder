import pathlib
from datetime import datetime

from django.core.cache import cache
from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import render, redirect
from django.views import View
from reminder_app.forms import ChangeAccountDataForm
from reminder_app.models import User

from tools_for_views import email_check


class ChangeAccountDataPage(View):
    def get(self, request, data_to_change, token):
        # если в redis БД нет переданного токена, то доступ блокируется
        if not cache.get(token):
            raise PermissionDenied()
        # --- --- --- ---
        user = User.objects.get(id=cache.get(token))
        form = ChangeAccountDataForm()
        return render(request, 'authed/change_account_data.html',
                      {'title': 'Смена данных профиля',
                       'header': 'Смена данных профиля', "token": token,
                       "user": user, "data_to_change": data_to_change,
                       "data_to_change_current_value": getattr(user,data_to_change),
                       "form": form, })

    def post(self, request, data_to_change, token):
        user = User.objects.get(id=cache.get(token))
        form = ChangeAccountDataForm(request.POST, request.FILES)
        if form.is_valid():
            new_value = form.cleaned_data["new_value"]
            new_avatar = form.cleaned_data["new_avatar"]
            # валидация полей формы
            if new_avatar:
                if user.avatar != "static/media/avatars/cat_developer.jpg":
                    pathlib.Path(f"{user.avatar}").unlink()
                user.avatar = new_avatar
            elif new_value:
                if data_to_change == "name":
                    user.name = new_value
                elif data_to_change == "email":
                    if email_check(new_value):
                        user.email = new_value
                    else:
                        raise ValidationError("Некорректный email")
                elif data_to_change == "password":
                    if len(new_value) < 5 or not any(char.isdigit() for char in new_value) or not any(
                            char.isalpha() for char in new_value):
                        raise ValidationError("Пароль должен быть более 5-ти символов, а также содержать цифры")
                    else:
                        user.password = new_value
                elif data_to_change == "birthdate":
                    try:
                        datetime.strptime(new_value, "%Y-%m-%d")
                        user.birthdate = new_value
                    except ValueError:
                        raise ValidationError("Пожалуйста, введите дату рождения в следующем формате: 'ГГГГ-ММ-ДД' ")
            if not new_value and not new_avatar:
                raise ValidationError("Пожалуйста, заполните все необходимые поля")
            # --- --- ---
            user.save()
            return redirect(f'/account/{token}')

        return render(request, 'authed/change_account_data.html',
                      {'title': 'Смена данных профиля',
                       'header': 'Смена данных профиля', "token": token,
                       "user": user, "data_to_change": data_to_change,
                       "data_to_change_current_value": getattr(user, data_to_change),
                       "form": form, })
