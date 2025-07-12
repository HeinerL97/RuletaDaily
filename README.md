🎯 RuletaDaily

RuletaDaily es una aplicación web desarrollada con Python y Django que permite gestionar una lista de participantes y realizar selecciones aleatorias en un entorno de trabajo, como reuniones daily. Su objetivo es brindar una experiencia ágil, visual y sencilla para dinamizar equipos.

🚀 Características

🎡 Ruleta aleatoria para seleccionar participantes.

👥 Gestión de participantes por proyecto.

💾 Manejo de lista temporal para evitar modificar la base de datos hasta confirmar cambios.

🔒 Confirmaciones con modal antes de actualizar información.

💡 Separación de lógica entre datos persistentes y temporales.

🖥️ Interfaz interactiva con tarjetas clicables y diseño moderno.

🧰 Requisitos

Python 3.x

Django 4.x o superior


⚙️ Instalación

Clona el repositorio:

git clone https://github.com/HeinerL97/RuletaDaily.git
cd RuletaDaily

Crea y activa un entorno virtual:

python -m venv venv
venv\Scripts\activate  # En Windows
# o en Linux/macOS
source venv/bin/activate

Instala las dependencias:

pip install -r requirements.txt

Realiza las migraciones:

python manage.py migrate

Ejecuta el servidor de desarrollo:

python manage.py runserver

Accede en tu navegador a:

http://127.0.0.1:8000/

🗂️ Estructura del Proyecto

RuletaDaily/  
├── daily_roulette/        # Lógica de la ruleta diaria  
├── env/                   # Entorno virtual (no se sube al repo)  
├── Login/                 # Módulo de autenticación  
├── media/                 # Archivos subidos por los usuarios (si aplica)  
├── participants/          # Gestión de participantes  
├── proyecto/              # Módulo de proyectos  
├── registro/              # Creación de usuario  
├── static/                # Archivos estáticos: CSS, JS, imágenes  
├── templates/             # Archivos HTML (interfaces del sistema)  
├── .gitignore             # Archivos/Carpetas que Git debe ignorar  
├── db.sqlite3             # Base de datos SQLite (para desarrollo)  
├── manage.py              # Script principal de Django  
├── README.md              # Documentación del proyecto  
└── requirements.txt       # Dependencias del proyecto  


📬 Contacto
Desarrollado por Heiner Urrego.¿Dudas o sugerencias? ¡Estoy abierto a feedback y colaboraciones!