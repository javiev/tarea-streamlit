# Usar una imagen base de Python
FROM python:3.9

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar las dependencias necesarias para h5py
RUN apt-get update && apt-get install -y \
    libhdf5-dev \
    libc6-dev

# Instalar Poetry
RUN pip install poetry

# Copiar archivos de configuración de Poetry
COPY pyproject.toml /app/

# Configurar Poetry para no crear un entorno virtual
RUN poetry config virtualenvs.create false

# Instalar dependencias
RUN poetry install

# Copiar el resto del código fuente
COPY . /app

# Exponer el puerto de Streamlit
EXPOSE 8501

# Ejecutar Streamlit
CMD ["streamlit", "run", "app.py"]
