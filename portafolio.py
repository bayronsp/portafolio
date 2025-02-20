import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", page_icon="🎯", layout="centered")

# Estilo CSS para personalizar el fondo y el footer
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

# Proyecto 1: Chatbot
col1, col2 = st.columns([1, 2])
with col1:
    st.image("./images/chatbot.png", caption="Chatbot ALOHA VIRTUAL", use_column_width=True)  # Reemplaza con la ruta de tu imagen
with col2:
    if st.button("Explorar Chatbot ALOHA VIRTUAL"):
        st.markdown("[Ir al proyecto](https://aloha-virtual.streamlit.app)", unsafe_allow_html=True)

# Proyecto 2: Visualización de datos de peatones
col3, col4 = st.columns([1, 2])
with col3:
    st.image("./images/peatones.png", caption="Visualización de Peatones", use_column_width=True)  # Reemplaza con la ruta de tu imagen
with col4:
    if st.button("Explorar Visualización de Peatones"):
        st.markdown("[Ir al proyecto](https://peatones.streamlit.app)", unsafe_allow_html=True)

# Proyecto 3: Proyecto adicional
col5, col6 = st.columns([1, 2])
with col5:
    st.image("./images/proyecto_adicional.png", caption="Proyecto Adicional", use_column_width=True)  # Reemplaza con la ruta de tu imagen
with col6:
    if st.button("Explorar Proyecto Adicional"):
        st.markdown("[Ir al proyecto](https://proyecto-adicional.streamlit.app)", unsafe_allow_html=True)

# Mensaje adicional
st.write("¡Gracias por visitar mi portafolio! Si quieres más información, no dudes en contactarme. 😊")
