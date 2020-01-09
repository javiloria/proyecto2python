from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import EstatusPropuesta, Tranzabilidad
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt
import datetime



@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'estatusPropuesta/index.html'
    context_object_name = 'estatusPropuestas_list'    
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='Abrio el panel de un estatus de propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return EstatusPropuesta.objects.order_by('id')

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEstatusPropuestaView(generic.CreateView):
    model = EstatusPropuesta
    fields = "__all__"
    template_name = 'estatusPropuesta/create.html'
    def form_valid(self, form):
        term = form.save(commit=False)
        term.save()
        p = Tranzabilidad(tipo_de_acccion='Creo un estatus de propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'El estatus de la propuesta se creo exitosamente')
        return redirect('estatusPropuestas:estatusPropuestas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateEstatusPropuestaView(generic.UpdateView):
    model = EstatusPropuesta
    fields = "__all__"
    template_name = 'estatusPropuesta/update.html'
    def form_valid(self, form):
        estatusPropuesta = form.save(commit=False)
        estatusPropuesta.save()        
        p = Tranzabilidad(tipo_de_acccion='actualizo un estatus de propuesta', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'El estatus de la propuesta se actualizada exitosamente')
        return redirect('estatusPropuestas:estatusPropuestas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEstatusPropuestaView(generic.DeleteView):
    model = EstatusPropuesta
    template_name = 'estatusPropuesta/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino un estatus de propuestas', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('estatusPropuestas:estatusPropuestas_list')


@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_estatusPropuesta_xls(generic.ArchiveIndexView):
    def export_estatusPropuesta_xls(request):
        model = EstatusPropuesta
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="estatusPropuesta.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('estatusPropuesta')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Nombre' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = EstatusPropuesta.objects.all().values_list('id','nombre').order_by('id')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel los estatus de propuestas', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response    