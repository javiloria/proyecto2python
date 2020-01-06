from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorador import *
from django.contrib.auth.decorators import login_required
from ..models import User
import math

@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'list_users'
    def get_queryset(self):
        return User.objects.order_by('cedula')

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'

opciones=['cedula', 'esAdmin', 'esGestor', 'esInvitado', 'username', 'password', 'type', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'ucab_email', 'email', 'telefono', 'telefono_1', 'observaciones']

@method_decorator([login_required, gestor_permisos], name='dispatch')
class BusquedaUsuario(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'list_users'
    def get_queryset(self):
        if self.request.GET:
            cedula = self.request.GET.get('search')
            if cedula == "":
                return User.objects.order_by('cedula')
            if not str.isdigit(cedula):
                return User.objects.filter(primer_nombre = str(cedula))
        return User.objects.filter(cedula = int(cedula))

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateUserView(generic.CreateView):
    model = User
    fields = opciones
    template_name = 'user/create.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request,  'usuario creado exitosamente')
        return redirect('users:users_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateUserView(generic.UpdateView):
    model = User
    fields = opciones
    template_name = 'user/update.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        messages.success(self.request, 'usuario actualizado exitosamente')
        return redirect('users:users_list')


@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users:users_list')
