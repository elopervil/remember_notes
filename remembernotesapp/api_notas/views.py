from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api_notas.serializers import NotesSerializer
from panelNotes.models import Notes


class NotesAPIView(APIView):

    def get(self, request):
        notes = Notes.objects.all()
        notes_serializer = NotesSerializer(notes, many=True)
        return Response(data=notes_serializer.data)


class NotesViewset(viewsets.ModelViewSet):

    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
