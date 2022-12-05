from rest_framework import serializers
from panelNotes.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('pub_date',)
        read_only_fields = ('owner_user',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Notes.objects.create(**validated_data, owner_user=user)