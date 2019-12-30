from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import EstatusTG
from django.utils.decorators import method_decorator
from ..decorador import *

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'estatusTG/index.html'
    context_object_name = 'estatusTGs_list'    
    def get_queryset(self):
        return EstatusTG.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEstatusTGView(generic.CreateView):
    model = EstatusTG
    fields = "__all__"
    template_name = 'estatusTG/create.html'
    def form_valid(self, form):
        estatusTG = form.save(commit=False)
        estatusTG.save()
        messages.success(self.request, 'El estatus del TG se creo exitosamente')
        return redirect('estatusTGs:estatusTGs_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateEstatusTGView(generic.UpdateView):
    model = EstatusTG
    fields = "__all__"
    template_name = 'estatusTG/update.html'
    def form_valid(self, form):
        estatusTG = form.save(commit=False)
        estatusTG.save()
        messages.success(self.request, 'El estatus del TG se actualizo exitosamente')
        return redirect('estatusTGs:estatusTGs_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEstatusTGView(generic.DeleteView):
    model = EstatusTG
    template_name = 'estatusTG/delete.html'
    success_url = reverse_lazy('estatusTGs:estatusTGs_list')