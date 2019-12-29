# Generated by Django 3.0.1 on 2019-12-28 22:37

from django.db import migrations, models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'El usuario ya existe!!'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='usuario')),
                ('password', models.CharField(max_length=128, verbose_name='contraseña')),
                ('esAdmin', models.BooleanField(default=False)),
                ('esManager', models.BooleanField(default=False)),
                ('esInvitado', models.BooleanField(default=False)),
                #esto te lo crea por defecto DJANGO python
                #porque estamos usando el user del mismo django
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                 ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                 ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),

            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PRO', 'Profesor'), ('EST', 'Estudiante'), ('AFU', 'Afuera')], max_length=20, verbose_name='tipo')),
    			('cedula_id' , models.IntegerField(unique=True, verbose_name="cédula") ),
			    ('primer_nombre' , models.CharField(max_length=100, verbose_name="primer nombre")),
			    ('segundo_nombre' , models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo nombre")),
			    ('primer_apellido' , models.CharField(max_length=100, verbose_name="primer apellido")),
			    ('segundo_apellido' , models.CharField(max_length=100, null=True, blank=True, verbose_name="segundo apellido")),
			    ('ucab_email' , models.CharField(max_length=100,verbose_name="correo ucab", null=True, blank=True)),
			    ('email' ,models.CharField(max_length=100, verbose_name="correo personal")),
			    ('telefono' , models.CharField(max_length=15, verbose_name="teléfono 1")),
			    ('telefono_1' ,models.CharField(max_length=15, verbose_name="teléfono 2", null=True, blank=True)),
	        ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),            
        migrations.CreateModel(
            name='Termin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='código terminología (Ej:201915)')),
            	('descripcion', models.CharField(max_length=50, verbose_name="descripción")),
            ],
            options={
                'verbose_name': 'Terminología',
                'verbose_name_plural': 'Terminologías',
            },
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('entrega_fecha', models.DateTimeField(verbose_name='fecha de entrega')), 
			    ('titulo' , models.CharField(max_length=200,verbose_name="título")),
			    ('estatus' ,models.CharField(max_length=30, verbose_name="estatus de la propuesta")),
			    ('estudiante_1' ,models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name="propuesta_estudiante_1", to='gestorAppTG.Persona', verbose_name="estudiante 1")),
			    ('estudiante_2' , models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, null=True, blank=True, related_name="propuesta_estudiante_2",  to='gestorAppTG.Persona',verbose_name="estudiante 2")),
			    ('tutor_academico' , models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="propuesta_tutor_academico", to='gestorAppTG.Persona', verbose_name="tutor académico")),
			    ('tutor_empresa' , models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="propuesta_tutor_empresa", to='gestorAppTG.Persona', verbose_name="tutor empresarial")),
			    ('termin' , models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name="propuesta_termin",  to='gestorAppTG.Termin',verbose_name="terminología en la que se entrego")),
			],
            options={
                'verbose_name': 'Propuesta',
                'verbose_name_plural': 'Propuestas',
            },
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
			    ('titulo', models.CharField(max_length=200, null=True, blank=True, verbose_name="título")),
			    ('estatus', models.CharField(max_length=30, verbose_name="estatus")),
			    ('nrc', models.IntegerField(verbose_name="código NRC")),
			    ('descriptors', models.CharField(max_length=50, verbose_name="descriptores")),
			    ('categoriaTema', models.CharField(max_length=50, verbose_name="categoría temática")),
			    ('fechaTope', models.DateTimeField(verbose_name="fecha tope de entrega")),
			    ('EmpresaNombre', models.CharField(max_length=100, verbose_name="nombre de la empresa")),
			    ('termin', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name="termin_tesis", to='gestorAppTG.Termin', verbose_name="terminología")),
			    ('propuesta', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, related_name="propuestaTesis",to='gestorAppTG.Propuesta', verbose_name="propuesta asociada")),
	          ],
            options={
                'verbose_name': 'Tesis',
                'verbose_name_plural': 'Tesis',
            },
        ),
        migrations.CreateModel(
            name='Defensa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
			    ('fecha_defensa', models.DateTimeField(verbose_name="fecha de la defensa")),
			    ('jurado_1',models.BooleanField(default=False,verbose_name="jurado 1 ")),
			    ('jurado_2', models.BooleanField(default=False,verbose_name="jurado 2 ")),
			    ('jurado_3', models.BooleanField(default=False,verbose_name="jurado 3 ")),
			    ('calificacion', models.IntegerField(verbose_name="calificación")),
			    ('mencion_publicacion', models.BooleanField(default=False,verbose_name="mención publicación")),
			    ('mencion_honorifica', models.BooleanField(default=False,verbose_name="mención honorífica")),
			    ('correcciones', models.BooleanField(default=False,verbose_name="se entregaron correcciones")),
			    ('fecha_correciones', models.DateTimeField(verbose_name="fecha tope de correcciones")),
			    ('calificacion_mod', models.BooleanField(default=False,verbose_name="se subió la calificación")),
			    ('observaciones', models.CharField(max_length=500,verbose_name="observaciones", null=True, blank=True)),
			    ('tesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="tesisDefensa",  to='gestorAppTG.Tesis',verbose_name="tesis adjunta")),
            ],
            options={
                'verbose_name': 'Defensa',
                'verbose_name_plural': 'Defensas',
            },
        ),
    ]
