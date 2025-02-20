import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Portafolio Bayron Salas",
    page_icon=":briefcase:",
    layout="wide",
)

# Variable para controlar la navegación entre hojas
if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "Sobre mí"

# Estilos CSS personalizados
st.markdown(
    """
    <style>
    /* Fondo general */
    body {
        background-color: #F9F9F9; /* Fondo gris súper claro */
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #E0E0E0; /* Fondo gris más oscuro */
    }

    [data-testid="stSidebar"] h1 {
        text-align: center; /* Centrar el texto */
        color: #1E3A8A; /* Azul profesional */
        font-weight: bold; /* Negrita */
    }

    /* Botones en sidebar */
    .stButton button {
        color: #1E3A8A; /* Azul profesional */
        background-color: white; /* Fondo blanco */
        border: 2px solid #1E3A8A; /* Borde azul */
        border-radius: 8px; /* Bordes redondeados */
        font-size: 16px; /* Tamaño de texto */
        font-weight: bold; /* Negrita */
        margin-bottom: 10px; /* Espaciado */
    }
    .stButton button:hover {
        background-color: #1E3A8A; /* Fondo azul al pasar el ratón */
        color: white; /* Texto blanco al pasar el ratón */
    }

    /* Header principal */
    .header {
        text-align: center;
        margin-bottom: 50px;
    }
    .header h1 {
        font-size: 48px;
        font-weight: bold;
        color: #1E3A8A; /* Azul profesional */
    }
    .header h1 span {
        color: #F59E0B; /* Mostaza */
    }
    .header p {
        font-size: 20px;
        color: #4B5563; /* Gris oscuro */
    }
    .profile-image {
        border-radius: 50%;
        border: 4px solid #F59E0B; /* Mostaza */
        max-width: 160px;
        margin-top: 20px;
    }

    /* Estilo de enlaces de proyectos */
    .project img {
        width: 300px;
        border: 3px solid #F59E0B; /* Mostaza */
        border-radius: 12px;
    }
    .project img:hover {
        border-color: #1E3A8A; /* Azul profesional al pasar el ratón */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Función "Sobre mí"
def sobremi():
    st.markdown(
        """
        <div class="header">
            <img src="https://raw.githubusercontent.com/bayronsp/portafolio/main/images/profile.png" alt="Profile Image" class="profile-image"
            style="width:150px; height:auto; border-radius:50%;">
            <h1>Hola, soy <span>Bayron Salas Ponce</span></h1>
            <p>Ingeniero Civil Industrial especializado en Ciencia de Datos y Sistemas Inteligentes.</p>
            <p>Apasionado por la optimización de procesos y el análisis basado en datos.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Función "Análisis de Datos"
def analisis_datos():
    st.title("Proyectos de Análisis de Datos")

    # Proyecto de peatones
    peatones_url = "https://peatones.streamlit.app/#b4f9fe1a"
    st.header("Visualización de Peatones")
    st.markdown(
        f"""
        <div class="project">
            <a href="{peatones_url}" target="_blank">
                <img src="https://raw.githubusercontent.com/bayronsp/portafolio/main/images/peatones.png" alt="Visualización de Peatones">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar
st.sidebar.title("Navegación")

# Contenedor principal para organizar botones
with st.sidebar.container():
    if st.button("Sobre mí"):
        st.session_state.pagina_actual = "Sobre mí"
    if st.button("Análisis de Datos"):
        st.session_state.pagina_actual = "analisis_datos"

# Control de navegación entre páginas
pagina = st.session_state.get("pagina_actual", "Sobre mí")

# Mostrar contenido basado en la página seleccionada
if pagina == "Sobre mí":
    sobremi()
elif pagina == "analisis_datos":
    analisis_datos()
