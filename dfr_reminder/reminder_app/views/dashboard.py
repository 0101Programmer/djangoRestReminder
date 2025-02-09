import pathlib
from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.core.cache import cache
from django.core.exceptions import PermissionDenied, ValidationError
from reminder_app.models import User, Note
from django.core.paginator import Paginator
from reminder_app.forms import AddNoteForm, ChangeNoteStatusForm


class DashboardPage(View):
    def get(self, request, token):
        # если в redis БД нет переданного токена, то доступ блокируется
        if not cache.get(token):
            raise PermissionDenied()
        # --- --- --- ---
        user = User.objects.get(id=cache.get(token))
        notes = user.notes.all().order_by('id')
        completed_notes = user.notes.filter(is_completed=True)
        uncompleted_notes = user.notes.filter(is_completed=False)
        add_note_form = AddNoteForm(initial={'user': user})
        change_note_status_form = ChangeNoteStatusForm()

        # пагинатор
        paginator = Paginator(notes, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # --- --- --- ---

        return render(request, 'authed/dashboard.html',
                      {'title': 'Дашборд',
                       'header': 'Список напоминаний', "add_note_form": add_note_form,
                       "change_note_status_form": change_note_status_form, "token": token, "page_obj": page_obj,
                       "notes_len": len(notes), "completed_notes": completed_notes, "uncompleted_notes": uncompleted_notes})

    def post(self, request, token):
        user = User.objects.get(id=cache.get(token))
        add_note_form = AddNoteForm(request.POST, request.FILES, initial={'user': user})
        change_note_status_form = ChangeNoteStatusForm(request.POST)
        if add_note_form.is_valid():
            add_note_form.save()
            return redirect(f'/dashboard/{token}')
        elif change_note_status_form.is_valid():
            note_id = change_note_status_form.cleaned_data["note_id"]
            note = Note.objects.get(id=note_id)
            if 'status_update' in request.POST:
                if note.is_completed is True:
                    note.is_completed = False
                else:
                    note.is_completed = True
                note.save()
            elif 'delete_note' in request.POST:
                if note.image:
                    pathlib.Path(f"{note.image}").unlink(missing_ok=True)
                note.delete()
            return redirect(f'/dashboard/{token}')
        raise ValidationError("Something went wrong, please try again.")
