from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorador import *
from django.contrib.auth.decorators import login_required
from ..models import Persona


@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'persona/index.html'
    context_object_name = 'list_personas'
    
    def get_queryset(self):
        return Persona.objects.order_by('primer_nombre')[:5]

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Persona
    template_name = 'persona/detail.html'


@method_decorator([login_required, manager_permisos], name='dispatch')
class CreatePersonView(generic.CreateView):
    model = Persona
    fields = "__all__"
    template_name = 'persona/create.html'

    def form_valid(self, form):
        persona = form.save(commit=False)
        persona.save()
        messages.success(self.request,  'persona creada exitosamente')
        return redirect('personas:personas_list')


@method_decorator([login_required, manager_permisos], name='dispatch')
class UpdatePersonView(generic.UpdateView):
    model = Persona
    fields = "__all__"
    template_name = 'persona/update.html'

    def form_valid(self, form):
        persona = form.save(commit=False)
        persona.save()
        messages.success(self.request, 'persona actualizada exitosamente')
        return redirect('personas:personas_list')


@method_decorator([login_required, manager_permisos], name='dispatch')
class DeletePersonView(generic.DeleteView):
    model = Persona
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('personas:personas_list')
