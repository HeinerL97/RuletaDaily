from django.shortcuts import render, redirect
from participants.models import Participant
import random

def roulette_view(request):
    participants = list(Participant.objects.all())
    selected = None
    if request.method == 'POST' and participants:
        selected = random.choice(participants)
        selected.delete()
        return render(request, 'roulette/roulette.html', {'selected': selected, 'participants': participants})
    return render(request, 'roulette/roulette.html', {'selected': selected, 'participants': participants})