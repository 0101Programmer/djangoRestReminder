from rest_framework import serializers
from reminder_app.models import User, Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'birthdate', 'avatar')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image', 'remind_date', 'is_completed', 'user')
