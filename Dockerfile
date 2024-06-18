# Usar una imagen base de Python 3.11
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el contenido local al directorio de trabajo del contenedor
COPY . .

# Instalar las dependencias de la aplicación y Reflex en el contenedor
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Inicializar la aplicación Reflex
RUN reflex init

# Descargar todas las dependencias npm y compilar el frontend
RUN reflex export --frontend-only --no-zip

# Copiar script de inicialización de la base de datos
COPY init_db.sql /docker-entrypoint-initdb.d/


# Configurar la señal de parada hasta que Reflex maneje SIGTERM correctamente
STOPSIGNAL SIGKILL

# Ejecutar migraciones antes de iniciar el backend
CMD [ -d alembic ] && reflex db migrate; reflex run --env prod
