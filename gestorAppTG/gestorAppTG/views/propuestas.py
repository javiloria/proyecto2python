from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Propuesta
from django.utils.decorators import method_decorator
from ..decorador import *
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'propuestas/index.html'
    context_object_name = 'propuestas_listass'
    
    def get_queryset(self):
        return Propuesta.objects.order_by('entrega_fecha')

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Propuesta
    template_name = 'propuestas/detail.html'

@method_decorator([login_required, gestor_permisos], name='dispatch')
class BusquedaPropuesta(generic.ListView):
    template_name = 'propuestas/index.html'
    context_object_name = 'propuestas_listass'
    def get_queryset(self):
        if self.request.GET:
            search = self.request.GET.get('search')
            if search == "":
                return Propuesta.objects.order_by('entrega_fecha')
        return Propuesta.objects.filter(Q(titulo = str(search)) | Q(estatus__nombre = str(search))) 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreatePropuestaView(generic.CreateView):
    model = Propuesta
    fields = "__all__"
    template_name = 'propuestas/create.html'
    def clean(self):
        cleaned_data = super().clean()
        raise forms.ValidationError(
            "Did not send for 'help' in the subject despite "
            "CC'ing yourself."
        )
    def form_valid(self, form):
        propuesta = form.save(commit=False)
        if(propuesta.estudiante_1.getId()== propuesta.estudiante_2.getId()):
            messages.error(self.request, 'Error no puede ser el mismo estudiante en la misma propuesta.')
            def my_function(request, backend): data = "AJA" 
            return redirect('propuestas:propuestas_create',my_function)
        else:    
            propuesta.save()
            messages.success(self.request, 'La propuesta fue creada exitosamente')
            return redirect('propuestas:propuestas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdatePropuestaView(generic.UpdateView):
    model = Propuesta
    fields = "__all__"
    template_name = 'propuestas/update.html'
    def form_valid(self, form):
        propuesta = form.save(commit=False)
        propuesta.save()
        messages.success(self.request, 'La propuesta fue actualizada exitosamente')
        return redirect('propuestas:propuestas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeletePropuestaView(generic.DeleteView):
    model = Propuesta
    template_name = 'propuestas/delete.html'
    success_url = reverse_lazy('propuestas:propuestas_list')