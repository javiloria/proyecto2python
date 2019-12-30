from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def admin_permisos(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    Deco = user_passes_test(
        lambda x: x.is_active and x.esAdmin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return Deco(function)
    return Deco

def gestor_permisos(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    Deco = user_passes_test(
        lambda x: x.is_active and (x.esGestor or x.esAdmin),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return Deco(function)
    return Deco

def invitado_permisos(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    Deco = user_passes_test(
        lambda x: x.is_active and (x.esGestor or x.esAdmin or x.esInvitado),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return Deco(function)
    return Deco