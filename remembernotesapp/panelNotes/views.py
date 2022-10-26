from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Notes
from .forms import AddNotesForm

# Create your views here.


def home_view(request):
    user_id = request.user.id
    if user_id is not None:
        notes = Notes.objects.filter(owner_user=user_id).order_by('done_date')
        return render(request, 'panelNotes/home.html', {
            "note_list": notes
        })
    else:
        return redirect('profiles:login')


def add_notes(request):
    if request.method == "POST":
        form = AddNotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            done_date = form.cleaned_data.get('done_date')
            pub_date = timezone.now()
            is_done = False
            owner_user = request.user
            reg_note = Notes.objects.create(
                title=title,
                description=description,
                pub_date=pub_date,
                done_date=done_date,
                is_done=is_done,
                owner_user=owner_user
            )
            reg_note.save()
            return redirect('panelNotes:home')
    else:
        form = AddNotesForm()

    return render(request, "panelNotes/addnotes.html", {'form': form})


def delete_notes(request, note_id):
    note = Notes.objects.get(pk=note_id)
    note.delete()
    return redirect('panelNotes:home')
