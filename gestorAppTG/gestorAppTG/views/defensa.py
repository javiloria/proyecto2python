from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Defensa
from django.utils.decorators import method_decorator
from ..decorador import *


@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'defensa/index.html'
    context_object_name = 'defensa_listass'
    def get_queryset(self):
        return Defensa.objects.order_by('id')[:5]

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Defensa
    template_name = 'defensa/detail.html'

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateDefensaView(generic.CreateView):
    model = Defensa
    fields = "__all__"
    template_name = 'defensa/create.html'
    def form_valid(self, form):
        defensa = form.save(commit=False)
        defensa.save()
        messages.success(self.request, 'La defensa fue creada exitosamente')
        return redirect('defensas:defensas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateDefensaView(generic.UpdateView):
    model = Defensa
    fields = "__all__"
    template_name = 'defensa/update.html'
    def form_valid(self, form):
        defensa = form.save(commit=False)
        defensa.save()
        messages.success(self.request, 'La defensa fue actualizada exitosamente')
        return redirect('defensas:defensas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteDefensaView(generic.DeleteView):
    model = Defensa
    template_name = 'defensa/delete.html'
    success_url = reverse_lazy('defensas:defensas_list')