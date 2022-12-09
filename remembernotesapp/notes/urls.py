from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('addnotes/', views.add_notes, name="addnotes"),
    path('addnotes/<int:note_id>/', views.delete_notes, name="deletenotes"),
    path('detail/<int:note_id>/', views.detail_notes, name="detailnotes"),
    path('editnotes/<int:note_id>', views.edit_notes, name="editnotes"),
]

