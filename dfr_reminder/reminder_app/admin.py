from django.contrib import admin
from reminder_app.models import User

# Register your models here.

try:
    admin.site.register(User)
finally:
    print('Hello from admin')
