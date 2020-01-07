from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import EstatusTG
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt


@method_decorator([login_required, admin_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'estatusTG/index.html'
    context_object_name = 'estatusTGs_list'    
    def get_queryset(self):
        return EstatusTG.objects.order_by('id')[:10]

@method_decorator([login_required, admin_permisos], name='dispatch')
class CreateEstatusTGView(generic.CreateView):
    model = EstatusTG
    fields = "__all__"
    template_name = 'estatusTG/create.html'
    def form_valid(self, form):
        estatusTG = form.save(commit=False)
        estatusTG.save()
        messages.success(self.request, 'El estatus del TG se creo exitosamente')
        return redirect('estatusTGs:estatusTGs_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class UpdateEstatusTGView(generic.UpdateView):
    model = EstatusTG
    fields = "__all__"
    template_name = 'estatusTG/update.html'
    def form_valid(self, form):
        estatusTG = form.save(commit=False)
        estatusTG.save()
        messages.success(self.request, 'El estatus del TG se actualizo exitosamente')
        return redirect('estatusTGs:estatusTGs_list')

@method_decorator([login_required, admin_permisos], name='dispatch')
class DeleteEstatusTGView(generic.DeleteView):
    model = EstatusTG
    template_name = 'estatusTG/delete.html'
    success_url = reverse_lazy('estatusTGs:estatusTGs_list')


@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_estatusTGs_xls(generic.ArchiveIndexView):
    def Export_estatusTGs_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="estatusTG.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('estatusTG')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['nombre' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = EstatusTG.objects.all().values_list('nombre').order_by('nombre')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response    