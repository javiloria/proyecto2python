# proyecto2python
## Integrantes:
* Ysabel Ardila --> ysabelardila
* José Barrientos --> Joseeli54
* Herick Navarro --> herick1
* Jorge Viloria --> javiloria

## ejecutar este proyecto
1. clone este repositorio

2. ejecute: Scripts\activate.bat 
	Esto para ejecutar el ambiente virtual

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
