# gunicorn_config.py

bind = '0.0.0.0:8000'
workers = 3
chdir = 'C:/Users/dsmar/Documents/django-portafolio'  # Ruta al directorio raíz del proyecto
pythonpath = 'C:/Users/dsmar/Documents/django-portafolio'  # Ruta al directorio que contiene tu aplicación Django
module = 'proyecto_django.wsgi'