from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Escuela
from django.utils.decorators import method_decorator
from ..decorador import *

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'escuela/index.html'
    context_object_name = 'escuelas_list'    
    def get_queryset(self):
        return Escuela.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEscuelaView(generic.CreateView):
    model = Escuela
    fields = "__all__"
    template_name = 'escuela/create.html'
    def form_valid(self, form):
        escuela = form.save(commit=False)
        escuela.save()
        messages.success(self.request, 'La escuela se creo exitosamente')
        return redirect('escuelas:escuelas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateEscuelaView(generic.UpdateView):
    model = Escuela
    fields = "__all__"
    template_name = 'escuela/update.html'
    def form_valid(self, form):
        escuela = form.save(commit=False)
        escuela.save()
        messages.success(self.request, 'La escuela se actualizada exitosamente')
        return redirect('escuelas:escuelas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEscuelaView(generic.DeleteView):
    model = Escuela
    template_name = 'escuela/delete.html'
    success_url = reverse_lazy('escuelas:escuelas_list')