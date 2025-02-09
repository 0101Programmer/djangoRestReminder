from rest_framework import generics
from reminder_app.models import Note
from reminder_app.serializers import NoteSerializer


class NoteAddAPIView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteListAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
