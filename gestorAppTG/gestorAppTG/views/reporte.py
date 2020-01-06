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
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import xlwt
import datetime

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte1View(generic.ListView):
    template_name = 'reporte/reporte1.html'
    context_object_name = 'propuesta_list_Reporte1'
    def get_queryset(self):
        rows1 = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_1__isnull=False).values_list('estudiante_1__cedula','estudiante_1__primer_apellido','estudiante_1__segundo_apellido','estudiante_1__primer_nombre','estudiante_1__segundo_nombre','termin__id','titulo', 'id') 
        rows = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_2__isnull=False).values_list('estudiante_2__cedula','estudiante_2__primer_apellido','estudiante_2__segundo_apellido','estudiante_2__primer_nombre','estudiante_2__segundo_nombre','termin__id','titulo', 'id').union(rows1) 
        return rows
        #reporte excluyendo a los que esten aprobados y poniendo 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte2View(generic.ListView):
    template_name = 'reporte/reporte2.html'
    context_object_name = 'propuesta_list_Reporte2'
    def get_queryset(self):
        rows1 = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_1__isnull=False).values_list('propuesta__estudiante_1__cedula','propuesta__estudiante_1__primer_apellido','propuesta__estudiante_1__segundo_apellido','propuesta__estudiante_1__primer_nombre','propuesta__estudiante_1__segundo_nombre','propuesta__termin__id','titulo', 'id') 
        rows = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_2__isnull=False).values_list('propuesta__estudiante_2__cedula','propuesta__estudiante_2__primer_apellido','propuesta__estudiante_2__segundo_apellido','propuesta__estudiante_2__primer_nombre','propuesta__estudiante_2__segundo_nombre','propuesta__termin__id','titulo', 'id').union(rows1) 
        return rows
        #reporte excluyendo a los que esten aprobados y poniendo 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte3View(generic.ListView):
    template_name = 'reporte/reporte3.html'
    context_object_name = 'propuesta_list_Reporte3'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #primer reporte filtar porque no sean aprobadas y por la cedula 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte4View(generic.ListView):
    template_name = 'reporte/reporte4.html'
    context_object_name = 'propuesta_list_Reporte4'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #segundo reporte filtar porque no sean aprobadas y por la cedula 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte5View(generic.ListView):
    template_name = 'reporte/reporte5.html'
    context_object_name = 'propuesta_list_Reporte5'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #primer reporte filtar porque no sean aprobadas y por la cedula 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte6View(generic.ListView):
    template_name = 'reporte/reporte6.html'
    context_object_name = 'propuesta_list_Reporte6'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #primer reporte filtar porque no sean aprobadas y por la cedula 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte7View(generic.ListView):
    template_name = 'reporte/reporte7.html'
    context_object_name = 'propuesta_list_Reporte7'
    def get_queryset(self):
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #segundo reporte filtar porque no sean aprobadas y por la cedula 
