# proyecto: gestorAppTG
## ambiente virtual --> proyecto2python

## Integrantes:
* Ysabel Ardila --> ysabelardila
* José Barrientos --> Joseeli54
* Herick Navarro --> herick1
* Jorge Viloria --> javiloria

## ¿ Como ejecutar este proyecto?
1. clone este repositorio

2. ejecutar: 	Scripts\activate.bat 
	* nota: Esto para ejecutar el ambiente virtual

3. pip install django 
	* nota: ESte paso solo se hace si no tenia django instalado

5. ejecutar: pip install -r requirements.txt

6. cd gestorAppTG

7. python manage.py migrate
	* nota: hacer este migrate solo la primera vez que se corra el proyecto 

7. python manage.py runserver 
	* nota: Al hacer este ultimo comando le deberia de aparecer algo como esto: 

	Django version 3.0.1, using settings 'gestorAppTG.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

6. En su navegador ejecutar: http://127.0.0.1:8000/

## Cosas que faltan por hacer:

* Hacer que la página inicial muestre algo alusivo al site las ultimas tres propuestas y las ultimas tres tesis, o las ultimas tres defensas

* evaluar la reincorporacion de los estatus de las propuestas y la de los estatus de las tesis

* evaluar el agregar, editar escuelas hay que hacer un nuevo crud

* Acciones que ha realizado cada usuario por periodo de fecha, El usuario que ejecuta cada transacción debe quedar registrado para trazabilidad.
 
* Exportar como pdf y como excel todas las consultas o todas las información

* ver como utilizar readthedocs

* cambiar esManager por esGestor

### consultas que hay que hacer:
* Lista de propuestas en estado diferentes de aprobadas, ordenadas por número de CI del
alumno y mostrar apellidos y nombres del alumno, TERM y nombre de la propuesta.

* Lista de TG en ejecución (estado diferente a aprobado), ordenados por número de CI del
alumno y mostrar apellidos y nombres del alumno, TERM y nombre del TG,

* Lista de Defensas no realizadas, ordenados por número de CI del alumno y mostrar apellidos
y nombres del alumno, TERM y nombre del TG

* Una consulta que permita desplegar una lista dependiendo del TERM, propuesta, TG o
defensa y estatus de estas. 

* Una consulta por selección de profesor que permita identificar las propuestas, TG o defensa
que tenga asignadas y que muestre el tipo de asignación (tutor, jurado, jurado suplente). 

* Una consulta por TERM que permita mostrar todas las propuestas, TG o defensas a realizar
en ese período. 

* Estadísticas: Al seleccionar uno o varios TERM debe mostrar una tabla de notas, media
aritmética, mediana, moda y desviación estándar de la selección. Este último debe ser
exportable a pdf.


### Errores: 

* al modificar la id de alguno y actualizas el no se va actualizar la id, sin enbargo si despues de eso eliminas y vuelve a cargar veras que se añadio uno nuevo con la id anterior que tu supuestamente cambiaste , arreglar esto

* en la pantalla de la propusta no esta validado que la propuesta el tutor sea diferente a los demas ni que los estudiantes se repitan , ni nada de eso

* hay que conectar user con persona (podemos unir user con persona)

* NRC cambiar y poner id

* Defensa hay que arreglar todo lo campos en el create, ademas de poner las limitantes de la calificacion y otras vainas