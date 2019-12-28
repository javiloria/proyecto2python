from django.db import models
from django.contrib.auth.models import AbstractUser
#TODO: VER LO DEL ATRIBUTOS UNIQUE
#TODO: VER SI TODOS LOS ATRIBUTOS FORANEOS LLEVAN ON_DELETE=MODELS.CASCADE
#TODO: CAMBIAR ENUM TYPE_CHOICES POR UN MODELO INDEPENDIENE

# Para la autenticacion y autorización
class User(AbstractUser):
    esAdmin = models.BooleanField(default=False)
    esManager = models.BooleanField(default=False)
    esInvitado = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


class Persona(models.Model):
    PROFESOR = 'PRO'
    ESTUDIANTE = 'EST'
    AFUERA = 'AFU'
    TYPE_CHOICES = [
        (PROFESOR, 'Profesor'),
        (ESTUDIANTE, 'Estudiante'),
        (AFUERA, 'Externo') #TODO: cambiar externo
    ]

    type = models.CharField(max_length=20,choices=TYPE_CHOICES, verbose_name="tipo")
    cedula_id = models.IntegerField(unique=True, verbose_name="cédula") 
    primer_nombre = models.CharField(max_length=100, verbose_name="primer nombre")
    segundo_nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo nombre")
    primer_apellido = models.CharField(max_length=100, verbose_name="primer apellido")
    segundo_apellido = models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo apellido")
    ucab_email = models.CharField(max_length=100,verbose_name="correo ucab", null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="correo personal")
    telefono = models.CharField(max_length=15, verbose_name="teléfono 1")
    telefono_1 = models.CharField(max_length=15, verbose_name="teléfono 2", null=True, blank=True)
    observaciones = models.CharField(max_length=500, verbose_name="observaciones", null=True, blank=True)

    def __str__(self):
        return self.primer_nombre + " " + self.primer_apellido

    #Opara setear el verbose_name 
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Termin(models.Model):    
    id = models.IntegerField(primary_key=True, verbose_name="código terminología")
    descripcion = models.CharField(max_length=50, verbose_name="descripción")
    def __str__(self):
        return str(self.id) + " (" + self.descripcion + ")"

    #para setear el verbose_name 
    class Meta:
        verbose_name = "Terminología"
        verbose_name_plural = "Terminologías"


class PropuestasEstatus(models.Model):
    
    nombre = models.CharField(max_length=20, verbose_name="nombre")

    def __str__(self):
        return self.nombre

    #para setear el verbose_name 
    class Meta:
        verbose_name = "Estado de la propuesta"
        verbose_name_plural = "Estados de las propuestas"


class TesisEstatus(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="nombre")
    def __str__(self):
        return self.nombre
    #para setear el verbose_name 
    class Meta:
        verbose_name = "Estado de la tesi"
        verbose_name_plural = "Estados de las tesis"

class Propuesta(models.Model):
    entrega_fecha = models.DateTimeField(verbose_name='fecha de entrega') 
    titulo = models.CharField(max_length=200,verbose_name="título")
    estatus = models.ForeignKey(PropuestasEstatus, on_delete=models.CASCADE, related_name="PropuestasEstatus",verbose_name="estatus de la propuesta")
    estudiante_1 = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="propuesta_estudiante_1", verbose_name="estudiante 1")
    estudiante_2 = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True, related_name="propuesta_estudiante_2", verbose_name="estudiante 2")
    tutor_academico = models.ForeignKey(Personaa, on_delete=models.CASCADE, related_name="propuesta_tutor_academico", verbose_name="tutor académico")
    tutor_empresa = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="propuesta_tutor_empresa", verbose_name="tutor empresarial")
    termin = models.ForeignKey(Termin, on_delete=models.CASCADE, related_name="propuesta_termin", verbose_name="terminología en la que se entrego")

    def __str__(self):
        return self.titulo

    def get_id(self):
        return self.id
    #para setear el verbose_name 
    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"


class Tesis(models.Model):

    id = models.CharField(max_length=100,primary_key=True)
    titulo = models.CharField(max_length=200, null=True, blank=True, verbose_name="título")
    estatus = models.ForeignKey(TesisEstatus, on_delete=models.CASCADE, related_name="TesisEstatus", verbose_name="estatus")
    nrc = models.IntegerField(verbose_name="código NRC")
    descriptors = models.CharField(max_length=50, verbose_name="descriptores")
    categoriaTema = models.CharField(max_length=50, verbose_name="categoría temática")
    fechaTope = models.DateTimeField(verbose_name="fecha tope de entrega")
    EmpresaNombre = models.CharField(max_length=100, verbose_name="nombre de la empresa")
    termin = models.ForeignKey(Termin, on_delete=models.CASCADE, related_name="termin_tesis", verbose_name="terminología")
    propuesta = models.ForeignKey(Propuesta, on_delete=models.CASCADE, related_name="propuestaTesis", verbose_name="propuesta asociada")


    def __str__(self):
        if self.titulo==None:
            return str(self.propuesta) 
        return self.titulo

    def save(self, *args, **kwargs):
        self.id = "TG-" + str(self.propuesta.get_id())
        super(Tesis, self).save(*args, **kwargs)

    #para setear el verbose_name 
    class Meta:
        verbose_name = "Tesis"
        verbose_name_plural = "Tesis"

class Defensa(models.Model):   

    fecha_defensa = models.DateTimeField(verbose_name="fecha de la defensa")
    jurado_1 = models.BooleanField(default=False,verbose_name="jurado 1 ")
    jurado_2 = models.BooleanField(default=False,verbose_name="jurado 2 ")
    jurado_3 = models.BooleanField(default=False,verbose_name="jurado 3 ")
    calificacion = models.IntegerField(verbose_name="calificación") #AGregar validacion de la calificacion
    mencion_publicacion = models.BooleanField(default=False,verbose_name="mención publicación")
    mencion_honorifica = models.BooleanField(default=False,verbose_name="mención honorífica")
    correcciones = models.BooleanField(default=False,verbose_name="se entregaron correcciones")
    fecha_correciones = models.DateTimeField(verbose_name="fecha tope de correcciones")
    calificacion_mod = models.BooleanField(default=False,verbose_name="se subió la calificación")
    observaciones = models.CharField(max_length=500,verbose_name="observaciones", null=True, blank=True)
    tesis = models.ForeignKey(Tesis, on_delete=models.CASCADE, related_name="tesisDefensa",verbose_name="tesis adjunta")

    def __str__(self):
        return str(self.fecha_defensa)
    
    #para setear el verbose_name 
    class Meta:
        verbose_name = "Defensa"
        verbose_name_plural = "Defensas"
