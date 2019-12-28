from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Termin
from django.utils.decorators import method_decorator
from ..decorador import *

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'termin/index.html'
    context_object_name = 'termin_list'    
    def get_queryset(self):
        return Termin.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateTerminView(generic.CreateView):
    model = Termin
    fields = "__all__"
    template_name = 'termin/create.html'
    def formu_valido(self, form):
        term = form.save(commit=False)
        term.save()
        messages.success(self.request, 'La terminología se creo exitosamente')
        return redirect('terms:terms_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateTerminView(generic.UpdateView):
    model = Termin
    fields = "__all__"
    template_name = 'termin/update.html'
    def formu_valido(self, form):
        termin = form.save(commit=False)
        termin.save()
        messages.success(self.request, 'La terminología se actualizada exitosamente')
        return redirect('termins:termins_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteTerminView(generic.DeleteView):
    model = Termin
    template_name = 'termin/delete.html'
    success_url = reverse_lazy('termins:termins_list')