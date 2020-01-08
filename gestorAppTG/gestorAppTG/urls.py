"""gestorAppTG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

#HERICK: importamos todas nuestras vistas aqui 
from .views import gestorAppTG
from .views import propuestas
from .views import user
from .views import tesis
from .views import termin
from .views import defensa
from .views import escuela
from .views import estatusTG
from .views import estatusPropuesta
from .views import reporte

urlpatterns = [
    
    path('', gestorAppTG.home, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls,  name="admin"),
    
    path('propuestas/', include(([
        path('', propuestas.IndexView.as_view(), name='propuestas_list'),
        path('<int:pk>/update/', propuestas.UpdatePropuestaView.as_view(), name='propuestas_update'),
        path('search/', propuestas.BusquedaPropuesta.as_view(), name='propuestas_search'),
        path('create/', propuestas.CreatePropuestaView.as_view(), name='propuestas_create'),
        path('<int:pk>/', propuestas.DetailView.as_view(), name='propuestas_details'),
		path('<int:pk>/delete/', propuestas.DeletePropuestaView.as_view(), name='propuestas_delete'),
        path('export/xls/', propuestas.Export_propuesta_xls.export_propuesta_xls, name='export_propuesta_xls'),
    ], 'gestorAppTG'), namespace='propuestas')),

    path('users/', include(([
        path('', user.IndexView.as_view(), name='users_list'),
        path('search/', user.BusquedaUsuario.as_view(), name='users_search'),
        path('<int:pk>/', user.DetailView.as_view(), name='users_details'),
        path('create/', user.CreateUserView.as_view(), name='users_create'),
        path('<int:pk>/update/', user.UpdateUserView.as_view(), name='users_update'),
        path('<int:pk>/delete/', user.DeleteUserView.as_view(), name='users_delete'),
        path('export/xls/', user.Export_users_xls.export_users_xls, name='export_users_xls'),
    ], 'gestorAppTG'), namespace='users')),

    path('tesis/', include(([
        path('', tesis.IndexView.as_view(), name='tesis_list'),
        path('create/', tesis.CreateTesisView.as_view(), name='tesis_create'),
        path('<str:pk>/', tesis.DetailView.as_view(), name='tesis_details'),
        path('<str:pk>/update/', tesis.UpdateTesisView.as_view(), name='tesis_update'),
        path('<str:pk>/delete/', tesis.DeleteTesisView.as_view(), name='tesis_delete'),
        path('export/xls/', tesis.Export_tesis_xls.export_tesis_xls, name='export_tesis_xls'),
    ], 'gestorAppTG'), namespace='tesis')),

    path('defensas/', include(([
        path('', defensa.IndexView.as_view(), name='defensas_list'),
        path('create/', defensa.CreateDefensaView.as_view(), name='defensas_create'),
        path('<str:pk>/', defensa.DetailView.as_view(), name='defensas_details'),
        path('<str:pk>/update/', defensa.UpdateDefensaView.as_view(), name='defensas_update'),
        path('<str:pk>/delete/', defensa.DeleteDefensaView.as_view(), name='defensas_delete'),
        path('export/xls/', defensa.Export_defensa_xls.export_defensa_xls, name='export_defensa_xls'),
    ], 'gestorAppTG'), namespace='defensas')),

    path('termin/', include(([
        path('', termin.IndexView.as_view(), name='termins_list'),
        path('create/', termin.CreateTerminView.as_view(), name='termin_create'),
        path('<int:pk>/update/', termin.UpdateTerminView.as_view(), name='termin_update'),
        path('<int:pk>/delete/', termin.DeleteTerminView.as_view(), name='termin_delete'),
        path('export/xls/', termin.Export_termin_xls.export_termin_xls, name='export_termin_xls')
    ], 'gestorAppTG'), namespace='termin')),

    path('estatusPropuestas/', include(([
        path('', estatusPropuesta.IndexView.as_view(), name='estatusPropuestas_list'),
        path('create/', estatusPropuesta.CreateEstatusPropuestaView.as_view(), name='estatusPropuestas_create'),
        path('<int:pk>/update/', estatusPropuesta.UpdateEstatusPropuestaView.as_view(), name='estatusPropuestas_update'),
        path('<int:pk>/delete/', estatusPropuesta.DeleteEstatusPropuestaView.as_view(), name='estatusPropuestas_delete'),
        path('export/xls/', estatusPropuesta.Export_estatusPropuesta_xls.export_estatusPropuesta_xls, name='export_estatusPropuesta_xls')
    ], 'gestorAppTG'), namespace='estatusPropuestas')),

    path('estatusTGs/', include(([
        path('', estatusTG.IndexView.as_view(), name='estatusTGs_list'),
        path('create/', estatusTG.CreateEstatusTGView.as_view(), name='estatusTGs_create'),
        path('<int:pk>/update/', estatusTG.UpdateEstatusTGView.as_view(), name='estatusTGs_update'),
        path('<int:pk>/delete/', estatusTG.DeleteEstatusTGView.as_view(), name='estatusTGs_delete'),
         path('export/xls/', estatusTG.Export_estatusTGs_xls.Export_estatusTGs_xls, name='export_estatusTGs_xls')
    ], 'gestorAppTG'), namespace='estatusTGs')),

    path('escuelas/', include(([
        path('', escuela.IndexView.as_view(), name='escuelas_list'),
        path('create/', escuela.CreateEscuelaView.as_view(), name='escuelas_create'),
        path('<int:pk>/update/', escuela.UpdateEscuelaView.as_view(), name='escuelas_update'),
        path('<int:pk>/delete/', escuela.DeleteEscuelaView.as_view(), name='escuelas_delete'),
        path('export/xls/', escuela.Export_escuela_xls.Export_escuela_xls, name='export_escuela_xls')
    ], 'gestorAppTG'), namespace='escuelas')),

    path('reporte1/', include(([
        path('', reporte.IndexReporte1View.as_view(), name='reporte1s_list'),
         path('export/xls/', reporte.Export_reporte1_xls.Export_reporte1_xls, name='export_reporte1_xls')
    ], 'gestorAppTG'), namespace='reporte1s')),
    path('reporte2/', include(([
        path('', reporte.IndexReporte2View.as_view(), name='reporte2s_list'),
         path('export/xls/', reporte.Export_reporte2_xls.Export_reporte2_xls, name='export_reporte2_xls')
    ], 'gestorAppTG'), namespace='reporte2s')),
    path('reporte3/', include(([
        path('', reporte.IndexReporte3View.as_view(), name='reporte3s_list'),
         path('export/xls/', reporte.Export_reporte3_xls.Export_reporte3_xls, name='export_reporte3_xls')
    ], 'gestorAppTG'), namespace='reporte3s')),
    path('reporte4/', include(([
        path('', reporte.IndexReporte4View.as_view(), name='reporte4s_list'),
         path('export/xls/', reporte.Export_reporte4_xls.Export_reporte4_xls, name='export_reporte4_xls')
    ], 'gestorAppTG'), namespace='reporte4s')),
    path('reporte5/', include(([
        path('', reporte.IndexReporte5View.as_view(), name='reporte5s_list'),
        path('export/xls/', reporte.Export_reporte5_xls.Export_reporte5_xls, name='export_reporte5_xls'),
        path('search/', reporte.Busqueda5.as_view(), name='reporte5_search'),
    ], 'gestorAppTG'), namespace='reporte5s')),
    path('reporte6/', include(([
        path('', reporte.IndexReporte6View.as_view(), name='reporte6s_list'),
         path('export/xls/', reporte.Export_reporte6_xls.Export_reporte6_xls, name='export_reporte6_xls')
    ], 'gestorAppTG'), namespace='reporte6s')),
    path('reporte7/', include(([
        path('', reporte.IndexReporte7View.as_view(), name='reporte7s_list'),
         path('export/xls/', reporte.Export_reporte7_xls.Export_reporte7_xls, name='export_reporte7_xls')
    ], 'gestorAppTG'), namespace='reporte7s')),
]
