from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import EstatusPropuesta
from django.utils.decorators import method_decorator
from ..decorador import *

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'estatusPropuesta/index.html'
    context_object_name = 'estatusPropuestas_list'    
    def get_queryset(self):
        return EstatusPropuesta.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEstatusPropuestaView(generic.CreateView):
    model = EstatusPropuesta
    fields = "__all__"
    template_name = 'estatusPropuesta/create.html'
    def formu_valido(self, form):
        term = form.save(commit=False)
        term.save()
        messages.success(self.request, 'El estatus de la propuesta se creo exitosamente')
        return redirect('estatusPropuestas:estatusPropuestas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateEstatusPropuestaView(generic.UpdateView):
    model = EstatusPropuesta
    fields = "__all__"
    template_name = 'termin/update.html'
    def formu_valido(self, form):
        estatusPropuesta = form.save(commit=False)
        estatusPropuesta.save()
        messages.success(self.request, 'El estatus de la propuesta se actualizada exitosamente')
        return redirect('termin:estatusPropuestas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEstatusPropuestaView(generic.DeleteView):
    model = EstatusPropuesta
    template_name = 'estatusPropuesta/delete.html'
    success_url = reverse_lazy('estatusPropuesta:estatusPropuestas_list')