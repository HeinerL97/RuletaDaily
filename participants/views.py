from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.files import File
from django.conf import settings

from .models import Participant
from proyecto.models import Proyecto
from .forms import ParticipantForm

import os
import json
import uuid
import shutil


def participantes_list(request, project_id):
    project = get_object_or_404(Proyecto, pk=project_id)
    participants = Participant.objects.filter(proyecto=project)

    participants_data = [
        {
            "id": p.id,
            "name": p.name,
            "image": p.image.url if p.image else ""
        }
        for p in participants
    ]

    form = ParticipantForm()
    return render(request, 'participants/list.html', {
        'participants': participants,
        'participants_json': json.dumps(participants_data),
        'form': form,
        'project': project
    })


@csrf_exempt
def agregar_participante_temporal(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data.get('image')

            image_url = ''
            filename = ''

            if image:
                ext = os.path.splitext(image.name)[1]
                unique_name = f"{uuid.uuid4().hex}{ext}"
                tmp_dir = os.path.join(settings.MEDIA_ROOT, 'tmp/participants')
                os.makedirs(tmp_dir, exist_ok=True)

                tmp_storage = FileSystemStorage(location=tmp_dir)
                filename = tmp_storage.save(unique_name, image)

                image_url = f"{settings.MEDIA_URL}tmp/participants/{filename}"

            participant_data = {
                'id': None,
                'name': name,
                'image': image_url
            }

            return JsonResponse({'success': True, 'participant': participant_data})
        return JsonResponse({'success': False, 'error': 'Datos inválidos'})
    return HttpResponseBadRequest("Método no permitido")


@csrf_exempt
def guardar_participantes(request, project_id):
    if request.method == 'POST':
        try:
            project = get_object_or_404(Proyecto, pk=project_id)
            data = json.loads(request.body)

            # IDs recibidos desde frontend
            ids_recibidos = {item.get("id") for item in data if item.get("id")}

            # Elimina los que ya no están
            actuales = Participant.objects.filter(proyecto=project)
            for p in actuales:
                if p.id not in ids_recibidos:
                    if p.image:
                        path = os.path.join(settings.MEDIA_ROOT, p.image.name)
                        if os.path.exists(path):
                            os.remove(path)
                    p.delete()

            # Crea o actualiza
            for item in data:
                participant_id = item.get("id")
                name = item.get("name")
                image_url = item.get("image")

                if participant_id:
                    participant = Participant.objects.filter(id=participant_id, proyecto=project).first()
                    if participant:
                        participant.name = name
                else:
                    participant = Participant(name=name, proyecto=project)

                # Procesa imagen solo si proviene de tmp
                if image_url and image_url.startswith(f"{settings.MEDIA_URL}tmp/participants/"):
                    relative_path = image_url.replace(settings.MEDIA_URL, '')
                    tmp_path = os.path.join(settings.MEDIA_ROOT, relative_path)

                    if os.path.exists(tmp_path):
                        final_dir = os.path.join(settings.MEDIA_ROOT, 'participants')
                        os.makedirs(final_dir, exist_ok=True)

                        final_filename = os.path.basename(tmp_path)
                        final_path = os.path.join(final_dir, final_filename)

                        shutil.move(tmp_path, final_path)

                        with open(final_path, 'rb') as f:
                            django_file = File(f)
                            participant.image.save(final_filename, django_file, save=False)

                participant.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return HttpResponseBadRequest("Método no permitido")


@csrf_exempt
def delete_participant(request, pk):
    if request.method == 'POST':
        participant = get_object_or_404(Participant, pk=pk)

        if participant.image:
            image_path = os.path.join(settings.MEDIA_ROOT, participant.image.name)
            if os.path.exists(image_path):
                os.remove(image_path)

        participant.delete()
        return JsonResponse({"success": True, "id": pk})

    return HttpResponseBadRequest("Método no permitido")