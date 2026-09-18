# API FastAPI - Usuarios y Libros

Este proyecto consiste en una API REST desarrollada con FastAPI. La API permite realizar operaciones CRUD para la gestión de usuarios y libros.

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Git y GitHub

## Entidades

La API trabaja con dos entidades principales:

### Usuarios
Permite:
- Crear usuarios
- Consultar usuarios
- Consultar un usuario por su ID
- Actualizar usuarios
- Eliminar usuarios

### Libros
Permite:
- Crear libros
- Consultar libros
- Consultar un libro por su ID
- Actualizar libros
- Eliminar libros

## Instalación

Para ejecutar el proyecto de forma local, primero se debe crear un entorno virtual:

```bash
python3 -m venv .venv
sudo apt install python3.14-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt



sudo apt install nodejs
nodejs -v
sudo apt install npm
sudo npm install pm2@latest -g

cd src
pm2 list
pm2 start "fastapi run"
