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

st.markdown(
    """
    <style>
    .stButton button {
        color: blue; /* Cambia el color del texto */
        background-color: white; /* Cambia el fondo */
        border: 2px solid blue; /* Agrega un borde */
        border-radius: 8px; /* Redondea las esquinas */
        font-size: 16px; /* Tamaño del texto */
        text-align: center;
        font-weight: bold; /* Texto en negrita */
        padding: 10px; /* Espaciado interno */
        margin-bottom: 10px; /* Espacio entre botones */
    }
    .stButton button:hover {
        background-color: blue; /* Fondo azul al pasar el ratón */
        color: white; /* Texto blanco al pasar el ratón */
    }
    [data-testid="stSidebar"] h1 {
        text-align: center; /* Centrar el texto */
        color: blue; /* Cambiar el color del texto */
        font-weight: bold; /* Negrita */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Función "Sobre mí"
def sobremi():
    # Estilos CSS personalizados
    st.markdown(
        """
        <style>
            .header {
                text-align: center;
                margin-bottom: 50px;
            }
            .header h1 {
                font-size: 48px;
                font-weight: bold;
                color: #1E3A8A;
            }
            .header h1 span {
                color: #F59E0B;
            }
            .header p {
                font-size: 20px;
                color: #4B5563;
            }
            .profile-image {
                border-radius: 50%;
                border: 4px solid #F59E0B;
                max-width: 160px;
                margin-top: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Encabezado principal
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

st.sidebar.title("Navegación")

# Contenedor principal para organizar botones
with st.sidebar.container():
    # Botones principales en la parte superior
    if st.button("Sobre mí"):
        st.session_state.pagina_actual = "Sobre mí"
    if st.button("Análisis de Datos"):
        st.session_state.pagina_actual = "analisis_datos"

# Control de navegación entre páginas
pagina = st.session_state.get("pagina_actual", "Sobre mí")  # Página predeterminada: "Sobre mí"

# Mostrar contenido basado en la página seleccionada
if pagina == "Sobre mí":
    sobremi()
elif pagina == "analisis_datos":
    analisis_datos()
