Ejecutar proyecto
=================
Esta guia le servira para ejecutar el proyecto siempre en caso de que no sea la primera vez que lo ejecuta
puede omitir el paso 6 ya que las migraciones estaran aplicadas

Paso 1: clone el  repositorio https://github.com/javiloria/proyecto2python.git ::

    git clone https://github.com/javiloria/proyecto2python.git

Paso 2: Active el ambiente virtual ejecutando::

    Scripts\activate.bat

Paso 3: Debe tener installar Django, ejecute el siguiente comando::

    pip install django

Paso 4: Debe instalar las dependecias del proyecto con el siguiente comando::

    pip install -r requirements.txt

Paso 5: Cambiese de directorio de la raiz a gestorAppTG con el siguiente comando::

    cd gestorAppTG


Paso 6: Aplicación de las migraciones::

    python manage.py migrate

Paso 7: Ejecucion del proyecto. Ejecute el siguiente comando::

    python manage.py runserver

Nota: si todo salio bien debe mostrarle en la consola el siguiente mensaje::

    Django version 3.0.1, using settings 'gestorAppTG.settings' Starting development server at 
    http://127.0.0.1:8000/ Quit the server with CTRL-BREAK.

