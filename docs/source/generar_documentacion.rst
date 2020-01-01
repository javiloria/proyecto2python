Generar documentación
=====================
Para generar la documentacion de Readthedocs existen 2 opciones de las cuales una es local y la otra 
es mediante el sitio web de Readthedocs http://readthedocs.org/ 

Opcion 1: Generación local
^^^^^^^^^^^^^^^^^^^^^^^^^^

Debe seguir los siguientes pasos:

Paso 1: Debe activar el ambiente virtual en caso de que no lo tenga activo ejecute el siguinte comando::

    Scripts\activate.bat

Paso 2: Debe cambiarse al directorio docs, si esta en el directorio raiz introduzca el siguiente comando::

    cd 'docs'

Paso 3: Para generar el html que contiene la documentación debe ejecutar el comando::

    make html

Paso 4: Para ver la documentación bastar con cambiarse al directorio /docs/build/html desde el terminal 
o desde el explorador de archivos y abrir el archivo index.html en el visualizará la documentación


Opcion 2: Mediante el sitio de Readthedocs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Paso 1: Debe autenticarse o crearse una cuenta en http://readthedocs.org/ 

Paso 2: Debe enlazar su repositorio de github con su cuenta.

Paso 3: Debe hacer click en su perfil para buscar la pestaña de Proyectos y en el seleccionar el proyecto deseado

Paso 4: Deje seleccionada la version latest y haga click en Build versión

Paso 5: Deberia mostrar un mensaje de "Compilación completada" en caso de que no haya error. Entonces 
puede ver la documentacion haciendo click en la pestaña "Ver documentación"