# 📸 Clasificador de Imágenes CIFAR-10

Alumno: [Javier Gómez C](https://javiev.dev)

Este proyecto es una aplicación de Streamlit que utiliza un modelo de Keras entrenado con el conjunto de datos CIFAR-10 para clasificar imágenes. La aplicación se ejecuta dentro de un contenedor Docker para asegurar un entorno de ejecución consistente y reproducible.

## 🟢 Requisitos

- Docker

> **Nota:** En Linux, Docker y Docker Compose deben instalarse por separado.

## 🗂 Estructura del Proyecto

```
├── app
│   ├── imagenes-ejemplo
│   │   ├── avion.jpg
│   │   └── perro.jpg
│   ├── app.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── model.keras
│   └── pyproject.toml
└── parte0
    ├── entrenamiento_modelo.ipynb
    └── pyproject.toml
```

### 📄 Descripción de Archivos

1. `app/app.py`: Script de Streamlit que carga el modelo y clasifica las imágenes subidas por el usuario.
2. `app/docker-compose.yml`: Archivo de configuración de Docker Compose para orquestar el contenedor de la aplicación.
3. `app/Dockerfile`: Archivo de configuración de Docker para crear la imagen de la aplicación.
4. `app/pyproject.toml`: Archivo de configuración de Poetry que define las dependencias del proyecto.
5. `app/model.keras`: El modelo preentrenado de Keras, serializado en **TensorFlow 2.17**.
6. `app/imagenes-ejemplo/avion.jpg` y `app/imagenes-ejemplo/perro.jpg`: Imágenes de ejemplo para probar el modelo.
7. `parte0/entrenamiento_modelo.ipynb`: Notebook de Jupyter para entrenar el modelo.
8. `parte0/pyproject.toml`: Archivo de configuración de Poetry para la parte de entrenamiento del modelo.

## 🚀 Ejecutar el Proyecto

1. Navega al directorio `app`:

   ```sh
   cd app
   ```

2. Construye y ejecuta el contenedor con Docker Compose:

   ```sh
   docker compose -p streamlit up --build
   ```

3. Abre tu navegador web y ve a `http://localhost:8501` para ver la aplicación de Streamlit.

## 🧪 Probar el Modelo

El modelo está entrenado para clasificar imágenes en las siguientes categorías del conjunto de datos CIFAR-10:
- Avión
- Auto
- Pájaro
- Gato
- Venado
- Perro
- Rana
- Caballo
- Barco
- Camión

Puedes subir las imágenes `avion.jpg` o `perro.jpg` a través de la interfaz de la aplicación para ver las predicciones del modelo. También puedes subir cualquier imagen en formato PNG, JPG o JPEG. Las imágenes pueden tener un tamaño de hasta 200MB.