from django.urls import path
from rest_framework import routers
from api_notas.views import NotesAPIView, NotesViewset


router = routers.SimpleRouter()
router.register(r'notes', NotesViewset)
urlpatterns = [
    path('notas/', NotesAPIView.as_view(), name='notas_api')
]
urlpatterns += router.urls
