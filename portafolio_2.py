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
            .timeline {
                margin: 50px auto;
                max-width: 900px;
            }
            .timeline-item {
                display: flex;
                align-items: center;
                margin-bottom: 40px;
                padding: 20px;
                background: #FFFFFF;
                border-radius: 12px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease;
            }
            .timeline-item:hover {
                transform: translateY(-10px);
            }
            .timeline-item-icon {
                width: 30px;
                height: 30px;
                background-color: #F59E0B;
                border-radius: 50%;
                flex-shrink: 0;
                margin-right: 20px;
            }
            .timeline-item-content {
                flex-grow: 1;
            }
            .timeline-item-title {
                font-size: 22px;
                font-weight: bold;
                color: #1E3A8A;
            }
            .timeline-item-company {
                font-size: 16px;
                color: #6B7280;
            }
            .timeline-item-description {
                font-size: 14px;
                color: #374151;
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Encabezado principal
    st.markdown(
        """
        <div class="header">
            <img src="https://via.placeholder.com/160" alt="Profile Image" class="profile-image">
            <h1>Hola, soy <span>Bayron Salas Ponce</span></h1>
            <p>Ingeniero Civil Industrial especializado en Ciencia de Datos y Sistemas Inteligentes.</p>
            <p>Apasionado por la optimización de procesos y el análisis basado en datos.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Línea de tiempo de experiencia laboral
    st.markdown(
        """
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-item-icon"></div>
                <div class="timeline-item-content">
                    <div class="timeline-item-title">Capstone Project - Proyecto de Titulación</div>
                    <div class="timeline-item-company">BRANDA SERVICIOS SPA - Ago 2024 – Ene 2025</div>
                    <div class="timeline-item-description">
                        Automatización de procesos y centralización de datos críticos en Power BI, logrando ahorros de más de $51 millones de pesos en el primer año.
                    </div>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-item-icon"></div>
                <div class="timeline-item-content">
                    <div class="timeline-item-title">Ayudante de Ciencia de Datos</div>
                    <div class="timeline-item-company">Universidad Católica del Norte - Ago 2023 – Ago 2024</div>
                    <div class="timeline-item-description">
                        Lideré la ejecución de laboratorios prácticos, desde regresión lineal hasta redes neuronales, apoyando a estudiantes en técnicas avanzadas.
                    </div>
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-item-icon"></div>
                <div class="timeline-item-content">
                    <div class="timeline-item-title">Práctica Preprofesional</div>
                    <div class="timeline-item-company">BST - Ene 2024 – Feb 2024</div>
                    <div class="timeline-item-description">
                        Desarrollo de un flujo ETL en Python para automatizar cargas a SQL Server, mejorando la eficiencia del procesamiento de datos.
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.title("Proyectos")

# Contenedor principal para organizar botones
with st.sidebar.container():
    # Botones principales en la parte superior
    if st.button("Modelos para la toma de decisiones multicriterio"):
        st.session_state.pagina_actual = "mcm"
    if st.button("Administración y planificación de la producción"):
        st.session_state.pagina_actual = "plani"
    if st.button("Proyectos de simulación y optimización del sistema de la producción"):
        st.session_state.pagina_actual = "simuio"
    if st.button("Modelo de visión por computadora para la detección y contabilización de objetos"):
        st.session_state.pagina_actual = "capstone"

# Contenedor adicional para colocar el botón "Sobre mí" al fondo
with st.sidebar.container():
    st.write("\n" * 100)  # Añadir un espacio vertical controlado
    if st.button("Sobre mí"):
        st.session_state.pagina_actual = "Sobre mí"

# Control de navegación entre páginas
pagina = st.session_state.get("pagina_actual", "mcm")  # Página predeterminada: "mcm"

# Mostrar contenido basado en la página seleccionada
if pagina == "mcm":
    st.title("Inicio")
    st.write("¡Bienvenido a la página principal!")
elif pagina == "plani":
    st.title("Hoja 1")
    st.write("Esta es la primera hoja.")
    numero = st.number_input("Ingresa un número:")
    st.write(f"El cuadrado del número es: {numero ** 2}")
elif pagina == "simuio":
    st.title("Hoja 2")
    st.write("Esta es la segunda hoja.")
    texto = st.text_input("Escribe algo aquí:")
    st.write(f"Escribiste: {texto}")
elif pagina == "capstone":
    st.title("Acerca de")
    st.write("Esta es una aplicación de ejemplo creada con Streamlit.")
elif pagina == "Sobre mí":
    sobremi()
