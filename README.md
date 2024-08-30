# TP20242-BACKEND
## Pasos a seguir para descargar e instalar el backend
### Requisitos
1. Tener Git instalado en tu computadora: https://git-scm.com/download/win , ver video tutorial para configurar el SSH entre Git y Github.
2. Tener Python 3.12.5 instalado en tu computadora: https://www.python.org/ , instalación customizada, next, clickear en "Add Python to environment variables", instalar
### Pasos para descargar el proyecto
1. Abrir la terminal de git con: Click derecho > Open Git Bash here
2. Escribir el comando: git clone https://github.com/Chablas/TP20242-BACKEND.git
3. Ir al drive https://drive.google.com/drive/folders/1xXMBGXzV_kZLHjTShuSSyLhA187Hy_Ks y copiar el contenido de DATABASE_URL.txt
4. Ir al directorio src/db/conexion.py y pegar el contenido en DATABASE_URL
5. En una terminal cualquiera (cmd, git bash o la terminal de vs code), ir al directorio donde clonaste el proyecto con el comando cd. 
Ejemplo: cd C:\Users\alumno\Downloads\TP20242-BACKEND
Para cambiar entre discos ssd a hdd o viceversa: d: o c:
Si están usando las computadoras de la u, eviten usar powershell porque a veces tira errores de permisos. De preferencia usar Command Prompt (cmd).
6. Crear el entorno virtual para que almacene las dependencias dentro del proyecto y no las instale globalmente en tu disco:
python -m venv nombredelentornovirtual (de preferencia llamarlo venv)
7. Abrir el entorno virtual: venv\Scripts\activate (asegurarse de estar en el directorio del proyecto)
Les debe salir: (venv) C:\Users\alumno\Downloads\TP20242-BACKEND
8. Escribir: pip install -r requirements.txt (esto instala las dependencias)

Con esto ya estaría instalado, ahora para iniciar el proyecto:
### Pasos para iniciar el proyecto
Una vez instalado, cada vez que quieran iniciar el proyecto, hacen:
9. Abrir el entorno virtual: venv\Scripts\activate (asegurarse de estar en el directorio del proyecto)
10. uvicorn src.main:app --reload
11. Dirigirse en su navegador web a http://localhost:8000/docs