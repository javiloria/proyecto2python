from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Escuela
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt

@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'escuela/index.html'
    context_object_name = 'escuelas_list'    
    def get_queryset(self):
        return Escuela.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEscuelaView(generic.CreateView):
    model = Escuela
    fields = "__all__"
    template_name = 'escuela/create.html'
    def form_valid(self, form):
        escuela = form.save(commit=False)
        escuela.save()
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
        messages.success(self.request, 'La escuela se actualizada exitosamente')
        return redirect('escuelas:escuelas_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEscuelaView(generic.DeleteView):
    model = Escuela
    template_name = 'escuela/delete.html'
    success_url = reverse_lazy('escuelas:escuelas_list')

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

        columns = ['Nombre' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Escuela.objects.all().values_list('nombre').order_by('nombre')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response    