from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from ..models import *
from django.utils.decorators import method_decorator
from ..decorador import *
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import xlwt
import datetime
from django.utils import timezone
from django.db.models import Count, F, Value

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte1View(generic.ListView):
    template_name = 'reporte/reporte1.html'
    context_object_name = 'propuesta_list_Reporte1'
    def get_queryset(self):
        rows1 = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_1__isnull=False).values_list('estudiante_1__cedula','estudiante_1__primer_apellido','estudiante_1__segundo_apellido','estudiante_1__primer_nombre','estudiante_1__segundo_nombre','termin__id','titulo', 'id') 
        rows = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_2__isnull=False).values_list('estudiante_2__cedula','estudiante_2__primer_apellido','estudiante_2__segundo_apellido','estudiante_2__primer_nombre','estudiante_2__segundo_nombre','termin__id','titulo', 'id').union(rows1) 
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 1', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return rows
        #reporte excluyendo a los que esten aprobados y poniendo 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte2View(generic.ListView):
    template_name = 'reporte/reporte2.html'
    context_object_name = 'propuesta_list_Reporte2'
    def get_queryset(self):
        rows1 = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_1__isnull=False).values_list('propuesta__estudiante_1__cedula','propuesta__estudiante_1__primer_apellido','propuesta__estudiante_1__segundo_apellido','propuesta__estudiante_1__primer_nombre','propuesta__estudiante_1__segundo_nombre','propuesta__termin__id','titulo', 'id') 
        rows = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_2__isnull=False).values_list('propuesta__estudiante_2__cedula','propuesta__estudiante_2__primer_apellido','propuesta__estudiante_2__segundo_apellido','propuesta__estudiante_2__primer_nombre','propuesta__estudiante_2__segundo_nombre','propuesta__termin__id','titulo', 'id').union(rows1) 
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 2', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return rows
        #reporte excluyendo a los que esten aprobados y poniendo 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte3View(generic.ListView):
    template_name = 'reporte/reporte3.html'
    context_object_name = 'propuesta_list_Reporte3'
    def get_queryset(self):
        rows1 = Defensa.objects.filter(fecha_defensa__date__gt=timezone.now(), tesis__propuesta__estudiante_1__isnull=False).values_list('tesis__propuesta__estudiante_1__cedula','tesis__propuesta__estudiante_1__primer_apellido','tesis__propuesta__estudiante_1__segundo_apellido','tesis__propuesta__estudiante_1__primer_nombre','tesis__propuesta__estudiante_1__segundo_nombre','tesis__propuesta__termin__id','tesis__titulo', 'tesis__id') 
        rows = Defensa.objects.filter(fecha_defensa__date__gt=timezone.now(), tesis__propuesta__estudiante_2__isnull=False).values_list('tesis__propuesta__estudiante_2__cedula','tesis__propuesta__estudiante_2__primer_apellido','tesis__propuesta__estudiante_2__segundo_apellido','tesis__propuesta__estudiante_2__primer_nombre','tesis__propuesta__estudiante_2__segundo_nombre','tesis__propuesta__termin__id','tesis__titulo', 'tesis__id').union(rows1) 
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 3', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return rows
        #reporte excluyendo a los que esten menores de esta fecha


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte4View(generic.ListView):
    template_name = 'reporte/reporte4.html'
    context_object_name = 'propuesta_list_Reporte4'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 4', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #segundo reporte filtar porque no sean aprobadas y por la cedula 


@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte5View(generic.ListView):
    template_name = 'reporte/reporte5.html'
    context_object_name = 'propuesta_list_Reporte5'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 5', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Defensa.objects.all()
 
@method_decorator([login_required, gestor_permisos], name='dispatch')
class Busqueda5(generic.ListView):
    template_name = 'reporte/reporte5.html'
    context_object_name = 'propuesta_list_Reporte5'
    def get_queryset(self):
        if self.request.GET:
            search = self.request.GET.get('search')
            if (search == ""):
                return Defensa.objects.all()
        p = Tranzabilidad(tipo_de_acccion='se busco en en el reporte 5', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Defensa.objects.filter(Q(jurado_1__primer_nombre = str(search)) | Q(jurado_2__primer_nombre = str(search)) | Q(jurado_auxiliar__primer_nombre = str(search)) | Q(tesis__propuesta__tutor_academico__primer_nombre = str(search)) | Q(tesis__propuesta__tutor_empresa__primer_nombre = str(search)) & Q(tesis__propuesta__tutor_academico__type = 'Profesor') | Q(tesis__propuesta__tutor_empresa__type = 'Profesor'))
        #reporte excluyendo a los que esten menores de esta fecha

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte6View(generic.ListView):
    template_name = 'reporte/reporte6.html'
    context_object_name = 'propuesta_list_Reporte6'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 6', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #primer reporte filtar porque no sean aprobadas y por la cedula 

@method_decorator([login_required, gestor_permisos], name='dispatch')
class IndexReporte7View(generic.ListView):
    template_name = 'reporte/reporte7.html'
    context_object_name = 'propuesta_list_Reporte7'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='se consulto el reporte 7', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        #segundo reporte filtar porque no sean aprobadas y por la cedula 

#EXPORTAR A EXCEL DE TODOS LOS REPORTEEEEEEEEEEEEEEEEEEEEEES

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte1_xls(generic.ArchiveIndexView):
    def Export_reporte1_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte1.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('estatusTG')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Cedula','Primer apellido','Segundo apellido','Primer Nombre','Segundo Nombre','Terminologia','Titulo','Id']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows1 = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_1__isnull=False).values_list('estudiante_1__cedula','estudiante_1__primer_apellido','estudiante_1__segundo_apellido','estudiante_1__primer_nombre','estudiante_1__segundo_nombre','termin__id','titulo', 'id') 
        rows = Propuesta.objects.exclude( estatus__nombre="Aprobada" ).filter(estudiante_2__isnull=False).values_list('estudiante_2__cedula','estudiante_2__primer_apellido','estudiante_2__segundo_apellido','estudiante_2__primer_nombre','estudiante_2__segundo_nombre','termin__id','titulo', 'id').union(rows1) 
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 1', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

#reporte 2

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte2_xls(generic.ArchiveIndexView):
    def Export_reporte2_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte2.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('estatusTG')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Cedula','Primer apellido','Segundo apellido','Primer Nombre','Segundo Nombre','Terminologia','Titulo TG','Id']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows1 = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_1__isnull=False).values_list('propuesta__estudiante_1__cedula','propuesta__estudiante_1__primer_apellido','propuesta__estudiante_1__segundo_apellido','propuesta__estudiante_1__primer_nombre','propuesta__estudiante_1__segundo_nombre','propuesta__termin__id','titulo', 'id') 
        rows = Tesis.objects.exclude( estatus__nombre="Aprobada" ).filter(propuesta__estudiante_2__isnull=False).values_list('propuesta__estudiante_2__cedula','propuesta__estudiante_2__primer_apellido','propuesta__estudiante_2__segundo_apellido','propuesta__estudiante_2__primer_nombre','propuesta__estudiante_2__segundo_nombre','propuesta__termin__id','titulo', 'id').union(rows1) 
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 2', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  
#reporte 3
@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte3_xls(generic.ArchiveIndexView):
    def Export_reporte3_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte3.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('estatusTG')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns =  ['Cedula','Primer apellido','Segundo apellido','Primer Nombre','Segundo Nombre','Terminologia','Titulo','Id']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows1 = Defensa.objects.filter(fecha_defensa__date__gt=timezone.now(), tesis__propuesta__estudiante_1__isnull=False).values_list('tesis__propuesta__estudiante_1__cedula','tesis__propuesta__estudiante_1__primer_apellido','tesis__propuesta__estudiante_1__segundo_apellido','tesis__propuesta__estudiante_1__primer_nombre','tesis__propuesta__estudiante_1__segundo_nombre','tesis__propuesta__termin__id','tesis__titulo', 'tesis__id') 
        rows = Defensa.objects.filter(fecha_defensa__date__gt=timezone.now(), tesis__propuesta__estudiante_2__isnull=False).values_list('tesis__propuesta__estudiante_2__cedula','tesis__propuesta__estudiante_2__primer_apellido','tesis__propuesta__estudiante_2__segundo_apellido','tesis__propuesta__estudiante_2__primer_nombre','tesis__propuesta__estudiante_2__segundo_nombre','tesis__propuesta__termin__id','tesis__titulo', 'tesis__id').union(rows1) 
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 3', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

#reporte 4
@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte4_xls(generic.ArchiveIndexView):
    def Export_reporte4_xls(request):
        model = Propuesta
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte4.xls"'

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
        rows = Propuesta.objects.filter(estatus__nombre="Aprobada").order_by('estudiante_1__cedula')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 4', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

#reporte 5
@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte5_xls(generic.ArchiveIndexView):
    def Export_reporte5_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte5.xls"'

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
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 5', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

#reporte 6
@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte6_xls(generic.ArchiveIndexView):
    def Export_reporte6_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte6.xls"'

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
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 6', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

#reporte 7

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_reporte7_xls(generic.ArchiveIndexView):
    def Export_reporte7_xls(request):
        model = EstatusTG
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="reporte7.xls"'

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
        p = Tranzabilidad(tipo_de_acccion='exporto en excel el reporte 7', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response  

        