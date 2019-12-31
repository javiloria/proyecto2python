from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import *
from django.utils.decorators import method_decorator
from ..decorador import *


@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'reporte1/index.html'
    context_object_name = 'propuesta_list_Reporte1'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')