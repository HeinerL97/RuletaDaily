from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto
from .forms import ProyectoForm

@login_required
def proyectos_list(request):
    proyectos = Proyecto.objects.filter(propietario=request.user)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.propietario = request.user
            proyecto.save()
            return redirect('proyecto:proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyecto/proyecto.html', {
        'proyectos': proyectos,
        'form': form,
    })

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, propietario=request.user)
    proyecto.delete()
    return redirect('proyecto:proyectos')