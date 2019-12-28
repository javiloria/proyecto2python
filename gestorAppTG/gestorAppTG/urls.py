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
from .views import persona
from .views import tesis
from .views import termin


urlpatterns = [
    
    path('', gestorAppTG.home, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    
    path('admin/', admin.site.urls,  name="admin"),
    
    path('propuestas/', include(([
        path('', propuestas.IndexView.as_view(), name='propuestas_list'),
        path('<int:pk>/update/', propuestas.UpdatePropuestaView.as_view(), name='propuestas_update'),
        path('create/', propuestas.CreatePropuestaView.as_view(), name='propuestas_create'),
        path('<int:pk>/', propuestas.DetailView.as_view(), name='propuestas_details'),
		path('<int:pk>/delete/', propuestas.DeletePropuestaView.as_view(), name='propuestas_delete')
    ], 'gestorAppTG'), namespace='propuestas')),

    path('personas/', include(([
        path('', persona.IndexView.as_view(), name='personas_list'),
        path('<int:pk>/', persona.DetailView.as_view(), name='personas_details'),
        path('create/', persona.CreatePersonaView.as_view(), name='personas_create'),
        path('<int:pk>/update/', persona.UpdatePersonaView.as_view(), name='personas_update'),
        path('<int:pk>/delete/', persona.DeletePersonaView.as_view(), name='personas_delete')
    ], 'gestorAppTG'), namespace='personas')),

    path('tesis/', include(([
        path('', tesis.IndexView.as_view(), name='tesis_list'),
        path('create/', tesis.CreateTesisView.as_view(), name='tesis_create'),
        path('<str:pk>/', tesis.DetailView.as_view(), name='tesis_details'),
        path('<str:pk>/update/', tesis.UpdateTesisView.as_view(), name='tesis_update'),
        path('<str:pk>/delete/', tesis.DeleteTesisView.as_view(), name='tesis_delete'),
    ], 'gestorAppTG'), namespace='tesis')),

    path('termin/', include(([
        path('', termin.IndexView.as_view(), name='termin_list'),
        path('create/', termin.CreateTerminView.as_view(), name='termin_create'),
        path('<int:pk>/update/', termin.UpdateTerminView.as_view(), name='termin_update'),
        path('<int:pk>/delete/', termin.DeleteTerminView.as_view(), name='termin_delete')
    ], 'gestorAppTG'), namespace='terms')),

]
