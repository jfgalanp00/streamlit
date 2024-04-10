import datetime
import pandas as pd
import streamlit as st
from PIL import Image# Permite definir que la función este en cache.

def main():
    """Generación de la webapp con streamlit"""
    
    # Definir título
    st.title("Título: Tutorial de Streamlit")    # Definir Header/Subheader

    st.header("Este es un header")

    st.subheader("Este es un subheader")    # Definir un Texto

    st.text("Texto: Hola Streamlit")    # Definición de Markdown

    st.markdown("# Este es un markdown h1 \n ## Este es un h2 \n ### Este es un h3")    

#hola

    st.header("Colores de texto y mensajes de error")

    st.success("Successful")

    st.info("Información!")

    st.warning("warning")

    st.error("Error")

    st.header("Widgets:")

    st.subheader("Checkbox")

    # Checkbox

    if st.checkbox("Show/Hide"):

        st.text("Mostrar u ocultar Widget")   



    st.subheader("Radio buttons")

    # Radio Buttons

    status = st.radio("Cual es su estatus", ("Activo", "Inactivo"))    

    if status == "Activo":

        st.success("Estas activo")

    else:

        st.warning("Inactivo")  




    st.subheader("SelectBox")

    # SelectBox

    occupation = st.selectbox(

        "Tu Ocupación", ["Programador", "Cientifico de datos", "Doctor", "Emprendedor"]

    )

    st.write("Opción seleccionada:", occupation)    



    st.subheader("MultiSelect")

    # MultiSelect

    location = st.multiselect(

        "Donde trabajas?",

        ("Londres", "Nueva York", "Accra", "Kiev", "Nepal", "Buenos Aires", "Caracas"),

    )

    st.write("Seleccionó:", len(location), "locaciones")    




    st.subheader("Slider")

    # Slider

    level = st.slider("Cual es tu nivel?", 1, 5)

    st.write("Nivel:", level) 




    st.subheader("Buttons")

    # Buttons

    if st.button("Acerca"):

        st.text("Streamlit es Cool")

    else:

        st.text("")    




    st.header("Como recibir una entrada y procesarla con streamlit?")

    st.subheader("Recibiendo texto")

    # Recibiendo texto

    firstname = st.text_input("Escriba su nombre:")

    if st.button("Aceptar"):

        result = firstname.title()

        st.success(result)   

    

    

    st.subheader("Área de texto")

    # Text Area

    message = st.text_area("Escriba un mensaje")

    if st.button("Aceptar "):

        result = message.title()

        st.success(result)    

    

    

    st.subheader("Entrada de fecha")

    # Date Input

    today = st.date_input("Hoy es", datetime.datetime.now())

    st.text(f"{today}")    




    st.subheader("Entrada de tiempo")

    # Time

    the_time = st.time_input("La hora es:", datetime.time())

    st.text(f"{the_time}")   




    st.header("Trabajar con archivos de imágenes, audio o vídeos")

    # Images    st.subheader("Archivo de imagen")

    img = Image.open("..\Streamlit\pages\perro.png")

    st.image(img, width=300, caption="Simple Imagen")    



    # Balloons

    st.balloons()    





if __name__ == "__main__":

    main()