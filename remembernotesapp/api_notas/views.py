from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)


from api_notas.serializers import NotesSerializer
from panelNotes.models import Notes


class NotesViewset(viewsets.ModelViewSet):

    serializer_class = NotesSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notes.objects.filter(owner_user=self.request.user)

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_token_api (request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please, enter username and password'}, status = HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid User'}, status=HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)
    

    