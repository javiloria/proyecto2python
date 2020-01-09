from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Termin, Tranzabilidad
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt
import datetime


@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'termin/index.html'
    context_object_name = 'termins_list'    
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='abrio el panel de terminologia', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Termin.objects.order_by('id')

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateTerminView(generic.CreateView):
    model = Termin
    fields = "__all__"
    template_name = 'termin/create.html'
    def form_valid(self, form):
        termin = form.save(commit=False)
        termin.save()
        p = Tranzabilidad(tipo_de_acccion='creo una terminologia', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La terminología se creo exitosamente')
        return redirect('termin:termins_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateTerminView(generic.UpdateView):
    model = Termin
    fields = "__all__"
    template_name = 'termin/update.html'
    def form_valid(self, form):
        termin = form.save(commit=False)
        termin.save()
        p = Tranzabilidad(tipo_de_acccion='actualizo una terminologia', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La terminología se actualizada exitosamente')
        return redirect('termin:termins_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteTerminView(generic.DeleteView):
    model = Termin
    template_name = 'termin/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino una terminologia', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('termin:termins_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_termin_xls(generic.ArchiveIndexView):
    def export_termin_xls(request):
        model = Termin
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="termin.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('termin')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Descripcion' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Termin.objects.all().values_list('id','descripcion').order_by('id')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel las terminologias', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response    