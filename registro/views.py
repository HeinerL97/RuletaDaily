from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroForm

def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Usuario creado correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, "registro/registro.html", {"form": form})