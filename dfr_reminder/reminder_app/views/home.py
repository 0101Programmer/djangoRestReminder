import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from reminder_app.models import User, Note


class GuestHomePage(View):
    def get(self, request):
        return render(request, 'guest/home.html', {'title': 'Главная страница', 'header': 'Главная страница'})


class AuthedUserHomePage(View):
    def get(self, request, token):
        # если в redis БД нет переданного токена, то доступ блокируется
        if not cache.get(token):
            raise PermissionDenied()
        # --- --- ---
        user = User.objects.get(id=cache.get(token))
        now = timezone.now()
        notes = user.notes.filter(remind_date__lt=now, is_completed=False).order_by('id')

        # пагинатор
        paginator = Paginator(notes, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # --- --- --- ---
        return render(request, 'authed/home.html',
                      {'title': 'Главная страница',
                       'header': 'Главная страница', "token": token, "page_obj": page_obj,
                       "notes_len": len(notes), })
