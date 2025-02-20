import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", page_icon="🎯", layout="centered")

# Título del portafolio
st.title("🌟 Mi Portafolio de Proyectos")
st.write("Bienvenido a mi portafolio. Aquí puedes explorar algunos de mis proyectos más destacados. ¡Haz clic en los enlaces para probarlos!")

# Lista de proyectos con hipervínculos
st.write("## Proyectos")
st.write("- [Chatbot: ALOHA VIRTUAL](https://aloha-virtual.streamlit.app)")
st.write("- [Visualización de datos de peatones](https://peatones.streamlit.app)")
st.write("- [Agrega aquí más proyectos...]")

# Mensaje adicional
st.write("¡Gracias por visitar mi portafolio! Si quieres más información, no dudes en contactarme. 😊")
