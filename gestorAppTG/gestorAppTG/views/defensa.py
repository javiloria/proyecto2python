from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import Defensa, Tranzabilidad
from django.utils.decorators import method_decorator
from ..decorador import *
import xlwt
import datetime
from django.db.models import Q


@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'defensa/index.html'
    context_object_name = 'defensa_listass'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se abrio el panel de defensa', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Defensa.objects.order_by('id')

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = Defensa
    template_name = 'defensa/detail.html'

@method_decorator([login_required, gestor_permisos], name='dispatch')
class BusquedaDefensa(generic.ListView):
    template_name = 'defensa/index.html'
    context_object_name = 'defensa_listass'
    def get_queryset(self):
        if self.request.GET:
            search = self.request.GET.get('search')
            p = Tranzabilidad(tipo_de_acccion='consulta de defensa', usuario=self.request.user,fecha_accion=datetime.datetime.now())
            p.save()
            if search == "":
                return Defensa.objects.order_by('id')
        return Defensa.objects.filter(Q(id__contains = str(search)) | Q(tesis__titulo__contains = str(search))) 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateDefensaView(generic.CreateView):
    model = Defensa
    fields = "__all__"
    template_name = 'defensa/create.html'
    def form_valid(self, form):
        defensa = form.save(commit=False)
        defensa.save()
        p = Tranzabilidad(tipo_de_acccion='creo una defensa', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La defensa fue creada exitosamente')
        return redirect('defensas:defensas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateDefensaView(generic.UpdateView):
    model = Defensa
    fields = "__all__"
    template_name = 'defensa/update.html'
    def form_valid(self, form):
        defensa = form.save(commit=False)
        defensa.save()
        p = Tranzabilidad(tipo_de_acccion='actualizo uan defensa', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'La defensa fue actualizada exitosamente')
        return redirect('defensas:defensas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteDefensaView(generic.DeleteView):
    model = Defensa
    template_name = 'defensa/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino una defensa', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('defensas:defensas_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_defensa_xls(generic.ArchiveIndexView):
    def export_defensa_xls(request):
        model = Defensa
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="defensa.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('defensa')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Fecha Defensa','Jurado 1','Jurado 2','Jurado auxiliar','calificacion','Observaciones','Tesis', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = Defensa.objects.all().select_related('jurado_1','jurado_2','jurado_auxiliar','tesis').values_list('id','fecha_defensa','jurado_1__primer_nombre','jurado_2__primer_nombre','jurado_auxiliar__primer_nombre','calificacion','observaciones','tesis__titulo').order_by('observaciones')
        rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in rows ]
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel las defensas', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response    