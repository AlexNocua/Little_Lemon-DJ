# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    gcc \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["gunicorn", "demoproject.wsgi:application", "--bind", "0.0.0.0:8000"]
