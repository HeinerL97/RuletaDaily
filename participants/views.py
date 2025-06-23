from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Participant
from .forms import ParticipantForm
import random

def main_view(request):
    participants = Participant.objects.all()
    selected = None
    timer = 60
    form = ParticipantForm()  # Siempre inicializa el form

    if request.method == 'POST':
        # Si el usuario envía el formulario de agregar participante
        if 'add' in request.POST:
            form = ParticipantForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['name']
                if Participant.objects.filter(name__iexact=name).exists():
                    messages.error(request, "¡Ya has participado hoy!")
                else:
                    form.save()
                    return redirect('main_view')
        # Si el usuario presiona el botón Random
        elif 'random' in request.POST:
            if participants:
                selected = random.choice(participants)
                timer = 60  # O el valor que desees
                # Eliminar el participante seleccionado
                selected.delete()

    context = {
        'participants': Participant.objects.all(),  # Refresca la lista después de eliminar
        'selected': selected,
        'timer': timer,
        'form': form,
    }
    return render(request, 'participants/list.html', context)

def delete_participant(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    participant.delete()
    return redirect('main_view')