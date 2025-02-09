from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from reminder_app.models import User

from reminder_app.forms import TokenExpirationForm, LogoutForm


class AccountPage(View):
    def get(self, request, token):
        # если в redis БД нет переданного токена, то доступ блокируется
        if not cache.get(token):
            raise PermissionDenied()
        # --- --- --- ---
        user = User.objects.get(id=cache.get(token))
        token_expiration = cache.ttl(token)

        logout_form = LogoutForm()
        token_expiration_form = TokenExpirationForm()
        return render(request, 'authed/account.html', {'title': 'Личный кабинет',
                                                       'header': 'Личный кабинет', "token": token, "user": user,
                                                       "token_expiration": token_expiration, "logout_form": logout_form,
                                                       "token_expiration_form": token_expiration_form,})

    def post(self, request, token):
        user = User.objects.get(id=cache.get(token))
        token_expiration = cache.ttl(token)

        logout_form = LogoutForm(request.POST)
        token_expiration_form = TokenExpirationForm(request.POST)

        if token_expiration_form.is_valid():
            cache.set(token, user.id, int(token_expiration_form.cleaned_data["exp_time"]))
            return redirect(f'/account/{token}')
        if logout_form.is_valid():
            cache.delete(token)
            return redirect('/')
        return render(request, 'authed/account.html', {'title': 'Личный кабинет',
                                                       'header': 'Личный кабинет', "token": token, "user": user,
                                                       "token_expiration": token_expiration, "logout_form": logout_form,
                                                       "token_expiration_form": token_expiration_form, })
