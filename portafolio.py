import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Portafolio", page_icon="🎯", layout="centered")

# Estilo para el footer fijo
footer_style = """
    <style>
        footer {visibility: hidden;}
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
    </style>
"""

st.markdown(footer_style, unsafe_allow_html=True)
st.markdown(
    """
    <div class="footer">
        📬 Conéctate conmigo: 
        <a href="https://www.linkedin.com/in/tuperfil" target="_blank">LinkedIn</a> |
        <a href="mailto:tuemail@gmail.com">Correo</a>
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
    st.image("https://via.placeholder.com/150", caption="Chatbot ALOHA VIRTUAL", use_column_width=True)
with col2:
    if st.button("Explorar Chatbot ALOHA VIRTUAL"):
        st.markdown("[Ir al proyecto](https://aloha-virtual.streamlit.app)", unsafe_allow_html=True)

# Proyecto 2: Visualización de datos de peatones
col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://via.placeholder.com/150", caption="Visualización de Peatones", use_column_width=True)
with col4:
    if st.button("Explorar Visualización de Peatones"):
        st.markdown("[Ir al proyecto](https://peatones.streamlit.app)", unsafe_allow_html=True)

# Puedes agregar más proyectos repitiendo el formato anterior
# Proyecto 3 (Ejemplo)
col5, col6 = st.columns([1, 2])
with col5:
    st.image("https://via.placeholder.com/150", caption="Proyecto Adicional", use_column_width=True)
with col6:
    if st.button("Explorar Proyecto Adicional"):
        st.markdown("[Ir al proyecto](https://proyecto-adicional.streamlit.app)", unsafe_allow_html=True)

# Mensaje adicional
st.write("¡Gracias por visitar mi portafolio! Si quieres más información, no dudes en contactarme. 😊")

