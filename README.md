# RuletaDaily

Proyecto desarrollado en Python con Django.

## Descripción

RuletaDaily es una aplicación web desarrollada con Django que permite gestionar y jugar a una ruleta diaria. El objetivo es ofrecer una experiencia interactiva y sencilla para los usuarios.

## Requisitos

- Python 3.x
- Django 4.x (o la versión que uses)
- (Opcional) Otros paquetes que utilices (añádelos aquí)

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/HeinerL97/RuletaDaily.git
   cd RuletaDaily
   ```

2. Crea y activa un entorno virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate   # En Windows
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Realiza las migraciones:
   ```sh
   python manage.py migrate
   ```

5. Ejecuta el servidor:
   ```sh
   python manage.py runserver
   ```

## Uso

Accede a `http://127.0.0.1:8000/` en tu navegador para comenzar a usar la aplicación.

## Estructura del proyecto

- `ruletadaily/` - Código fuente principal de Django
- `manage.py` - Script de administración de Django
- `requirements.txt` - Dependencias del proyecto

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT.