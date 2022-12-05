from django.urls import path
from rest_framework import routers
from api_notas.views import NotesViewset, get_token_api


router = routers.SimpleRouter()
router.register(r'notes', NotesViewset, basename='notes')
urlpatterns = [
    path('login/', get_token_api, name='get_token_api'),
]
urlpatterns += router.urls
