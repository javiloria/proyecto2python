from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Escuela, Tranzabilidad
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt
import datetime


@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'escuela/index.html'
    context_object_name = 'escuelas_list'    
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se abrio el panel de escuela', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Escuela.objects.order_by('id')

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEscuelaView(generic.CreateView):
    model = Escuela
    fields = "__all__"
    template_name = 'escuela/create.html'
    def form_valid(self, form):
        escuela = form.save(commit=False)
        escuela.save()
        p = Tranzabilidad(tipo_de_acccion='creo una escuela', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
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
        p = Tranzabilidad(tipo_de_acccion='actualizo una escuela', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La escuela se actualizada exitosamente')
        return redirect('escuelas:escuelas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEscuelaView(generic.DeleteView):
    model = Escuela
    template_name = 'escuela/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino una escuela', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('escuelas:escuelas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_escuela_xls(generic.ArchiveIndexView):
    def Export_escuela_xls(request):
        model = Escuela
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="escuelas.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('escuela')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Nombre' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Escuela.objects.all().values_list('id','nombre').order_by('id')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel las escuelas', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response    