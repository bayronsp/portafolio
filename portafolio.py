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
        .main {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            min-height: 100vh;
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

# Título principal
st.title("🌟 Mi Portafolio de Proyectos")
st.write("Bienvenido a mi portafolio. Aquí puedes explorar algunos de mis proyectos más destacados. ¡Haz clic en los botones para probarlos!")

# Espaciado
st.markdown("---")

# Estilo del enlace con HTML para hacer clic en la imagen
peatones_url = "https://peatones.streamlit.app/#b4f9fe1a"
st.header("Visualización de Peatones")
st.markdown(
    f"""
    <a href="{peatones_url}" target="_blank">
        <img src="https://raw.githubusercontent.com/bayronsp/portafolio/main/images/peatones.png" style="width:300px; border:none;"/>
    </a>
    """,
    unsafe_allow_html=True
)

# Pie de página
st.markdown("---")
# Mensaje adicional
st.write("¡Gracias por visitar mi portafolio! Si quieres más información, no dudes en contactarme. 😊")