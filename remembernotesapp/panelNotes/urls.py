from django.urls import path
from . import views

app_name = 'panelNotes'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('addnotes/', views.add_notes, name="addnotes"),
    path('addnotes/<int:note_id>/', views.delete_notes, name="deletenotes")
]
