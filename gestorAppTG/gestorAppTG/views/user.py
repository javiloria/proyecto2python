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



@method_decorator([login_required, invitado_permisos], name='dispatch')
class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'list_users'
    def get_queryset(self):
        p = Tranzabilidad(tipo_de_acccion='abrio el panel de usuario', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return User.objects.order_by('cedula')

@method_decorator([login_required, invitado_permisos], name='dispatch')
class DetailView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'

opciones=['cedula', 'esAdmin', 'esGestor', 'esInvitado', 'username', 'type', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'ucab_email', 'email', 'telefono', 'telefono_1', 'observaciones']
opciones1=['cedula', 'esAdmin', 'esGestor', 'esInvitado', 'username', 'password','type', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'ucab_email', 'email', 'telefono', 'telefono_1', 'observaciones']

@method_decorator([login_required, gestor_permisos], name='dispatch')
class BusquedaUsuario(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'list_users'
    def get_queryset(self):
        if self.request.GET:
            cedula = self.request.GET.get('search')
            p = Tranzabilidad(tipo_de_acccion='consulta de usuario por cedular', usuario=self.request.user,fecha_accion=datetime.datetime.now())
            p.save()
            if cedula == "":
                return User.objects.order_by('cedula')
            if not str.isdigit(cedula):
                return User.objects.filter(primer_nombre__contains = str(cedula))
        return User.objects.filter(cedula__contains = int(cedula))

@method_decorator([login_required, gestor_permisos], name='dispatch')
class CreateUserView(generic.CreateView):
    model = User
    fields = opciones1
    template_name = 'user/create.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        p = Tranzabilidad(tipo_de_acccion='creo a un usuario', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request,  'usuario creado exitosamente')
        return redirect('users:users_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateUserView(generic.UpdateView):
    model = User
    fields = opciones
    template_name = 'user/update.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        p = Tranzabilidad(tipo_de_acccion='actualizo a un usuario', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'Usuario actualizado exitosamente')
        return redirect('users:users_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class UpdateUserPassView(generic.UpdateView):
    model = User
    fields = ['username', 'password']
    template_name = 'user/updatePass.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.savePass()
        p = Tranzabilidad(tipo_de_acccion='actualizo la contraseña de un usuario', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        messages.success(self.request, 'contraseña actualizada exitosamente')
        return redirect('users:users_list')


@method_decorator([login_required, gestor_permisos], name='dispatch')
class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'user/delete.html'
    def get_success_url(self):
        p = Tranzabilidad(tipo_de_acccion='elimino a un usuario', usuario=self.request.user,fecha_accion=datetime.datetime.now())
        p.save()
        return reverse_lazy('users:users_list')

@method_decorator([login_required, gestor_permisos], name='dispatch')
class Export_users_xls(generic.ArchiveIndexView):
    def export_users_xls(request):
        model = User
        fields = "__all__"
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Cedula','Primer Apellido', 'Primer nombre', 'Usuario', 'Tipo','Email ucab', 'Email','Telefono' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = User.objects.all().values_list('cedula','primer_apellido','primer_nombre','username','type','ucab_email','email','telefono').order_by('cedula')
        
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        p = Tranzabilidad(tipo_de_acccion='exporto en excel los usuario', usuario=request.user,fecha_accion=datetime.datetime.now())
        p.save()
        wb.save(response)
        return response