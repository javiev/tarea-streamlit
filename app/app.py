import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

st.set_page_config(
    page_title="Clasificador de Imágenes CIFAR-10",
    page_icon=":camera:"
)

# Cargar el modelo con caché
@st.cache_resource
def load_model_from_file():
    return load_model('model.keras')

# Cargar el modelo
model = load_model_from_file()

st.title('Clasificador de Imágenes CIFAR-10')

uploaded_file = st.file_uploader("Sube una imagen para clasificar", type=["png", "jpg", "jpeg"])

# Procesa la imagen con caché
@st.cache_data
def process_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(32, 32))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

if uploaded_file is not None:
    img_array = process_image(uploaded_file)
    predictions = model.predict(img_array)
    class_names = ['avión', 'auto', 'pájaro', 'gato', 'venado', 'perro', 'rana', 'caballo', 'barco', 'camión']
    predicted_class = class_names[np.argmax(predictions)]
    predicted_proba = np.max(predictions) * 100

    st.write(f"La imagen es un: **{predicted_class}** con una probabilidad de {predicted_proba:.2f}%")
    st.image(uploaded_file, caption='Imagen Subida', use_column_width=True)