from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Propuesta,EstatusPropuesta, Tranzabilidad
from django.utils.decorators import method_decorator
from ..decorador import *
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import xlwt
import datetime

@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'propuestas/index.html'
    context_object_name = 'propuestas_listass'
    
    def get_queryset(self):    
        p = Tranzabilidad(tipo_de_acccion='consulto el panel de propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
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
            p = Tranzabilidad(tipo_de_acccion='busco una propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
            p.save()
            if search == "":
                return Propuesta.objects.order_by('entrega_fecha')
        return Propuesta.objects.filter(Q(titulo__contains = str(search)) | Q(estatus__nombre__contains = str(search))) 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreatePropuestaView(generic.CreateView):
    model = Propuesta
    fields = "__all__"
    template_name = 'propuestas/create.html'

    def form_valid(self, form):
        propuesta = form.save(commit=False)
        if(propuesta.estudiante_1.getId()== propuesta.estudiante_2.getId()):
            messages.error(self.request, 'Error no puede ser el mismo estudiante en la misma propuesta.')
            return redirect('propuestas:propuestas_create',my_function)
        else:    
            propuesta.save()
            p = Tranzabilidad(tipo_de_acccion='creo una propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
            p.save()
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
        p = Tranzabilidad(tipo_de_acccion='actualizo una propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La propuesta fue actualizada exitosamente')
        return redirect('propuestas:propuestas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeletePropuestaView(generic.DeleteView):
    model = Propuesta
    template_name = 'propuestas/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino una tesis', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('propuestas:propuestas_list')


@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_propuesta_xls(generic.ArchiveIndexView):
    def export_propuesta_xls(request):
        model = Propuesta
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="propuestas.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Título', 'Estatus', 'Escuela','Fecha de entrega','Estudiante 1 apellido','Estudiante 1 nombre','Estudiante 2 apellido','Estudiante 2 nombre','Tutor academico apellido','tutor academico nombre','Tutor empresarial apellido','Tutor empresarial nombre','Termin', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Propuesta.objects.all().select_related('estatus','escuela','estudiante_1','estudiante_2','tutor_academico','tutor_empresa','termin').values_list('titulo','estatus__nombre','escuela__nombre','entrega_fecha','estudiante_1__primer_apellido','estudiante_1__primer_nombre','estudiante_2__primer_apellido','estudiante_2__primer_nombre','tutor_academico__primer_apellido','tutor_academico__primer_nombre','tutor_empresa__primer_apellido','tutor_empresa__primer_nombre','termin__descripcion').order_by('estatus_id')
        
        rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel las propuestas', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response