from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def create_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('list_notes')
    return render(request, 'notes/create_note.html')

def list_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/list_notes.html', {'notes': notes})

@require_http_methods(["POST"])
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('list_notes')