from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Tesis
from django.utils.decorators import method_decorator
from ..decorador import *

@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'tesis/index.html'
    context_object_name = 'tesis_list'    
    def get_queryset(self):
        return Tesis.objects.order_by('id')[:10]

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Tesis
    template_name = 'tesis/detail.html'

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateTesisView(generic.CreateView):
    model = Tesis
    fields = "__all__"
    template_name = 'tesis/create.html'
    def form_valid(self, form):
        tesis = form.save(commit=False)
        tesis.save()
        messages.success(self.request, 'La tesis se creoo exitosamente')
        return redirect('tesis:tesis_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateTesisView(generic.UpdateView):
    model = Tesis
    fields =  "__all__"
    template_name = 'tesis/update.html'
    def form_valid(self, form):
        tesis = form.save(commit=False)
        tesis.save()
        messages.success(self.request, 'La propuesta se actualizo exitosamente')
        return redirect('tesis:tesis_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteTesisView(generic.DeleteView):
    model = Tesis
    template_name = 'tesis/delete.html'
    success_url = reverse_lazy('tesis:tesis_list')