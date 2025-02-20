import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", page_icon="🎯", layout="centered")

# Estilo CSS para personalizar fondo, botones e imagen
custom_style = """
    <style>
        body {
            background-color: #000000;  /* Fondo negro */
            color: #FFFFFF;  /* Texto blanco */
        }
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #1E1E1E;  /* Fondo del footer ligeramente diferente */
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            color: #FFFFFF;  /* Texto blanco */
        }
        .stButton button {
            background-color: #FF9E19;  /* Botón en color naranja */
            color: #000000;  /* Texto negro en botones */
            border-radius: 12px;
            border: none;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #AE431C;  /* Hover en rojo oscuro */
            color: #FFFFFF;
        }
        .project-container {
            text-align: center;
            padding: 20px;
        }
        .project-container img {
            max-width: 100%;
            border-radius: 12px;
        }
        .project-container a {
            text-decoration: none;
        }
    </style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# Footer fijo con tus datos
st.markdown(
    """
    <div class="footer">
        📬 Conéctate conmigo: 
        <a href="https://www.linkedin.com/in/bayronsalas/" target="_blank" style="color: #FF9E19;">LinkedIn</a> |
        <a href="mailto:bayron.sp5@gmail.com" style="color: #FF9E19;">Correo</a>
    </div>
    """, 
    unsafe_allow_html=True
)

# Título del portafolio
st.title("🌟 Mi Portafolio de Proyectos")
st.write("Bienvenido a mi portafolio. Aquí puedes explorar algunos de mis proyectos más destacados. ¡Haz clic en los botones para probarlos!")

# Función para crear un botón con imagen y texto
def project_button(image_path, caption, link):
    html_button = f"""
    <div class="project-container">
        <a href="{link}" target="_blank">
            <img src="{image_path}" alt="{caption}">
            <button>{caption}</button>
        </a>
    </div>
    """
    st.markdown(html_button, unsafe_allow_html=True)

# Proyectos en dos columnas
col1, col2 = st.columns(2)

# Proyecto 1: Chatbot
with col1:
    project_button(
        image_path="images/chatbot.png",  # Ruta local
        caption="Chatbot ALOHA VIRTUAL",
        link="https://aloha-virtual.streamlit.app"
    )

# Proyecto 2: Visualización de Peatones
with col2:
    project_button(
        image_path="images/peatones.png",  # Ruta local
        caption="Visualización de Peatones",
        link="https://peatones.streamlit.app"
    )

# Proyecto 3: Proyecto Adicional
with col1:
    project_button(
        image_path="images/proyecto_adicional.png",  # Ruta local
        caption="Proyecto Adicional",
        link="https://proyecto-adicional.streamlit.app"
    )

# Proyecto 4: Otro Proyecto
with col2:
    project_button(
        image_path="images/otro_proyecto.png",  # Ruta local
        caption="Otro Proyecto",
        link="https://otro-proyecto.streamlit.app"
    )

# Mensaje adicional
st.write("¡Gracias por visitar mi portafolio! Si quieres más información, no dudes en contactarme. 😊")