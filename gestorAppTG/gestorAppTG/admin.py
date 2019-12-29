from django.contrib import admin
from .models import Persona
from .models import Termin
from .models import Propuesta
from .models import Tesis
from .models import Defensa

admin.site.register(Persona)
admin.site.register(Termin)
admin.site.register(Propuesta)
admin.site.register(Tesis)
admin.site.register(Defensa)