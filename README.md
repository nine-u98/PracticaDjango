# Django-Portafolio

## Descripción
Es un portafolio donde puedes ver agregar tus proyectos creados.

## Autor
- [Carlos Daniel](https://github.com/nine-u98)

## Setup

Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
# windows
$ export venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego ejecutamos las migraciones para crear la base de datos de nuesta aplicacion, todo dentro de nuestro entorno virtual
```sh
# De manera general
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app

```sh
(env)$ python manage.py runserver
```
