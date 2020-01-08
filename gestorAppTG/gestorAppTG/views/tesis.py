from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Tesis
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt

@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'tesis/index.html'
    context_object_name = 'tesis_list'    
    def get_queryset(self):
        return Tesis.objects.order_by('id')

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Tesis
    template_name = 'tesis/detail.html'

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateTesisView(generic.CreateView):
    model = Tesis
    fields = "__all__"
    template_name = 'tesis/create.html'
    def form_valid(self, form):
        tesis = form.save(commit=False)
        tesis.save()
        messages.success(self.request, 'La tesis se creoo exitosamente')
        return redirect('tesis:tesis_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateTesisView(generic.UpdateView):
    model = Tesis
    fields =  "__all__"
    template_name = 'tesis/update.html'
    def form_valid(self, form):
        tesis = form.save(commit=False)
        tesis.save()
        messages.success(self.request, 'La propuesta se actualizo exitosamente')
        return redirect('tesis:tesis_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteTesisView(generic.DeleteView):
    model = Tesis
    template_name = 'tesis/delete.html'
    success_url = reverse_lazy('tesis:tesis_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_tesis_xls(generic.ArchiveIndexView):
    def export_tesis_xls(request):
        model = Tesis
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="tesis.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('tesis')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['NRC' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Tesis.objects.all().values_list('nrc').order_by('nrc')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response    