from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from ..decorador import *
from django.contrib.auth.decorators import login_required
from ..models import User, Tranzabilidad
import math
import xlwt
import datetime

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'tranzabilidad/index.html'
    context_object_name = 'list_tranzabilidad'
    def get_queryset(self):
        return Tranzabilidad.objects.order_by('usuario__cedula')

@method_decorator([login_required, admin_permisos], name='dispatch')
class BusquedaTranzabilidad(generic.ListView):
    template_name = 'tranzabilidad/index.html'
    context_object_name = 'list_tranzabilidad'
    def get_queryset(self):
        if self.request.GET:
            cedula = self.request.GET.get('search')
            if cedula == "":
                return Tranzabilidad.objects.order_by('usuario__cedula')
            if not str.isdigit(cedula):
                return Tranzabilidad.objects.filter(usuario__username= str(cedula))
        return Tranzabilidad.objects.filter(usuario__cedula = int(cedula))

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_tranzabilidad_xls(generic.ArchiveIndexView):
    def Export_tranzabilidad_xls(request):
        model = Tranzabilidad
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Tranzabilidad.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Tranzabilidad')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Cedula', 'Username','Primer Apellido', 'Primer nombre', 'fecha de la accion','tipo de accion realizada' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Tranzabilidad.objects.all().values_list('usuario__cedula','usuario__username','usuario__primer_apellido','usuario__primer_nombre','fecha_accion','tipo_de_acccion').order_by('usuario__cedula')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response