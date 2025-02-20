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
    [data-testid="stAppViewContainer"] {
        background-color: #0f091f !important; /* Usa !important para sobrescribir */
        color: #e0e0e0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0f0f2b; /* Fondo gris más oscuro */
        color: #ffffff;
    }

    [data-testid="stSidebar"] h1 {
        text-align: center; /* Centrar el texto */
        color: #ffffff; /* blanco */
        font-weight: bold; /* Negrita */
    }

    /* Botones en sidebar */
    .stButton button {
        background-color: #272640 !important; /* Fondo azul oscuro */
        color: #F9BF3B !important; /* Texto amarillo */
        border: 2px solid #F9BF3B !important; /* Borde amarillo */
        border-radius: 8px; /* Bordes redondeados */
        font-size: 16px; /* Tamaño del texto */
        font-weight: bold; /* Texto en negrita */
        padding: 10px;
        margin-bottom: 10px;
    }
    .stButton button:hover {
        background-color: #F9BF3B !important; /* Fondo amarillo en hover */
        color: #272640 !important; /* Texto azul oscuro */
    }

    /* Header principal */
    .header {
        text-align: center;
        margin-bottom: 50px;
    }
    .header h1 {
        font-size: 48px;
        font-weight: bold;
        color: #ffffff; /* Blanco */
    }
    .header h1 span {
        color: #cbe9f7; /* Gris azulado */
    }
    .header p {
        font-size: 20px;
        color: #ffffff; /* Blanco */
    }
    .profile-image {
        border-radius: 50%;
        border: 4px solid #cbe9f7; /* Gris azulado */
        max-width: 160px;
        margin-top: 20px;
    }

    /* Estilo de enlaces de proyectos */
    .project img {
        width: 300px;
        border: 3px solid #cbe9f7; /* celeste-gris */
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
