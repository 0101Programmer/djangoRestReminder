from django.forms import ModelForm, Form
from django import forms
from reminder_app.models import User, Note


class RegistrationForm(ModelForm):
    password_confirmation = forms.CharField(max_length=250, required=True, label="Подтверждение пароля")

    class Meta:
        model = User
        fields = ["name", "email", "password", "password_confirmation", "birthdate", "avatar"]
        labels = {
            'name': 'Имя',
            'email': 'Email',
            'password': 'Пароль',
            'birthdate': 'Дата рождения',
            'avatar': 'Фото профиля',
        }


class AddNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "image", "remind_date", "is_completed", "user"]
        labels = {
            'title': 'Название',
            'content': 'Описание',
            'image': 'Фото (опционально)',
            'remind_date': 'Напомнить в эту дату (опционально)',
            'is_completed': 'Завершено',
        }
        widgets = {'user': forms.HiddenInput(), "content": forms.Textarea(attrs={'rows': 1, 'cols': 40})}


class AuthorizationForm(Form):
    email = forms.CharField(max_length=250, required=True, label="Email")
    password = forms.CharField(max_length=250, required=True, label="Пароль")


class TokenExpirationForm(Form):
    TIME_CHOICES = (
        (300, "Пять минут"),
        (600, 'Десять минут'),
        (3_600, 'Час'),
        (3_600 * 24, '24 часа')
    )
    exp_time = forms.ChoiceField(choices=TIME_CHOICES, label="Обновить срок истечения токена "
                                                             "(токен истечёт через выбранный промежуток времени)")


class LogoutForm(Form):
    logout_btn = forms.CharField(widget=forms.HiddenInput(), required=False)


class ChangeNoteStatusForm(Form):
    note_id = forms.CharField(widget=forms.HiddenInput(), required=False)


class ChangeAccountDataForm(Form):
    new_value = forms.CharField(required=False, max_length=250, label="Новое значение")
    new_avatar = forms.ImageField(required=False, label="Новая фотография профиля")
