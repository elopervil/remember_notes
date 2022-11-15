from rest_framework import serializers
from panelNotes.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ['pub_date']
