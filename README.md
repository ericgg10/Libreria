# LIBRARY API
Esta es una API desarrollada con fastapi por Eric García en la que se podrán consultar los libros disponibles, realizar préstamos y devolver ejemplares. También se podrán gestionar los usuarios con seguridad mediante tokens.

## Instalación de UV
Uv es un gestor de paquetes extremadamente rápido para Python que nos servirá para limitar los paquetes que instalemos en nuestros proyectos. De este modo no tendremos que tener instalados todos los paquetes en los diferentes espacios de trabajo sino que tendremos instalados en cada espacio de trabajo los paquetes necesarios para poder trabajar.

### Instrucciones de instalación:
- Ejecutamos el terminal el CMD en Python y para instalarlo usaremos el comando:

    - Windows:
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    - Mac o Linux:
    curl -LsSf https://astral.sh/uv/install.sh | sh

### Comandos:
Para sincronizar las dependencias del proyecto con el entorno:
```
uv sync
```
Para ejecutar el entorno del proyecto:
```
uv run
```
Para agregar una dependencia al proyecto:
```
uv add
```
Para eliminar una dependencia del proyecto:
```
uv remove
```
Para ver el arbol de dependencias del proyecto:
```
uv tree
```

### Activar el entorno virtual:
Con este comando activaremos el entorno virtual donde se instalaran los paquetes y ejecuciones de Python:
```
.venv/bin/activate
```
## Ejecucción
Para lanzar el proyecto usaremos este comando:
```
uvicorn src.main:app --reload
```
Para ejecutar en la terminal el archivo sin que nos de error por el entorno:
```
python -m scripts.filename
```