import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 ,col4= st.columns(4)

with col1:
 
 st.subheader("Programacion Avanzada")
 image = Image.open('clase1.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://computoavanzada-pfrsyc2lbcyusesqgzdufg.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Calculo aplicado, gradiente")
 image = Image.open('clase2.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://computoavanzada-ddvhmauwtqruf9eyphgq8q.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Lógica, Big-O y Vectorización")
 image = Image.open('clase3.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://computoavanzada-69zzphwzxzdh2viahi9r7p.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Preparación de datos")
 image = Image.open('clase4.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://computoavanzada-sq8w4ad2m2xd9uyw2uorvk.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Aplicación Preparación de datos")
 image = Image.open('clase5.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://portafolio-de-computacion-avanzada-cgafnbkkxywuvdz7tvqml4.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Regresión Lineal")
 image = Image.open('clase6.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://computoavanzada-ku2n8rwpqjra8h45t9ujvs.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Series de Tiempo")
 image = Image.open('clase7.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://computoavanzada-dsog93gtgg3h9dh89rckmy.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Predicción y modelado de la calidad de aire")
 image = Image.open('clase8.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://computoavanzada-hmnrlfnkxatgwdkxj5snp2.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Prediccion de sensacion termica con lot")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


with col4: 
 st.subheader("De la regresión lineal a la logísitica")
 image = Image.open('clase10.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://computoavanzada-c7c3fmtonr6qqds9ypqbck.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Clasificación Knn")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Aplicación Knn Clasificación de fertilidad de  suelos")
 image = Image.open('clase12.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://computoavanzada-qqzzvlpfvvvelr4ksdhtkl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

