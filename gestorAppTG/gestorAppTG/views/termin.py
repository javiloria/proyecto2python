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
import xlwt


@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'termin/index.html'
    context_object_name = 'termins_list'    
    def get_queryset(self):
        return Termin.objects.order_by('id')[:5]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateTerminView(generic.CreateView):
    model = Termin
    fields = "__all__"
    template_name = 'termin/create.html'
    def form_valid(self, form):
        termin = form.save(commit=False)
        termin.save()
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
        messages.success(self.request, 'La terminología se actualizada exitosamente')
        return redirect('termin:termins_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteTerminView(generic.DeleteView):
    model = Termin
    template_name = 'termin/delete.html'
    success_url = reverse_lazy('termin:termins_list')


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

        columns = ['descripcion' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Termin.objects.all().values_list('descripcion').order_by('descripcion')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response    