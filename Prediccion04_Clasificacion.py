import streamlit as st
from joblib import load
import pandas as pd

# Cargar todos los modelos
modelos = {
    "Logistic Regression": load("Logistic Regression_pipeline_clasificacion.joblib"),
    "Decision Tree": load("Decision Tree_pipeline_clasificacion.joblib"),
    "Random Forest": load("Random Forest_pipeline_clasificacion.joblib"),
    "Gradient Boosting": load("Gradient Boosting_pipeline_clasificacion.joblib"),
    "SVM": load("SVM_pipeline_clasificacion.joblib"),
}

st.title("Prediccion transtorno de sueño")

# 1. Definimos la función de reinicio
def reset_values():
    st.session_state["nombre"] = ""
    st.session_state["genero"] = "Masculino"
    st.session_state["edad"] = 30
    st.session_state["ocupacion"] = "Ingeniero de software"

    st.session_state["du_suenio"] = 8.0
    st.session_state["ca_suenio"] = 5

    st.session_state["actividad"] = 30
    st.session_state["estres"] = 3
    st.session_state["imc"] = "Normal"
    st.session_state["presion"] = "140/90"
    st.session_state["fc"] = 75
    st.session_state["pasos"] = 3000
    st.session_state["trastorno"] = "Ninguno"

# 2. Agregamos el parámetro 'key' a cada widget para vincularlos
nombre_u = st.text_input("Nombre", "", key="nombre")
genero = st.selectbox("Género", ["Masculino", "Femenino"], key="genero")
edad = st.number_input("Edad", min_value=0, max_value=120, value=30, key="edad")
ocupacion = st.selectbox("Ocupación", ["Ingeniero de software", "Doctor", "Asesor de ventas", "Maestro", "Enfermera", "Ingeniero(a)", "Contador(a)", "Científico", "Abogado", "Vendedora", "Gerente"], key="ocupacion")

dur_suenio = st.number_input("Duración del sueño (0 - 10 Hrs)", min_value=0.0, max_value=10.0, value=8.0, key="du_suenio")
cal_suenio = st.number_input("Calidad del sueño (0 - 10)", min_value=0, max_value=10, value=5, key="ca_suenio")

actividad = st.number_input("Tiempo de actividad física diaria (0 - 90 min)", min_value=0, max_value=90, value=30, key="actividad")
estres = st.number_input("Nivel de estrés (0 - 8)", min_value=0, max_value=8, value=3, key="estres") 
imc = st.selectbox("Categoría de IMC", ["Normal", "Sobrepeso", "Obesidad", "Peso Normal"], key="imc")
presion = st.text_input("Presión arterial (100-160 / 60-100)", "140/90", key="presion")
fc = st.number_input("Frecuencia cardíaca (60 - 100)", min_value=60, max_value=100, value=75, key="fc")
pasos = st.number_input("Pasos diarios (3K - 10K)", min_value=3000, max_value=10000, value=3000, key="pasos")
# trastorno = st.selectbox("Trastorno del sueño", ["Ninguno", "Apnea del sueño", "Insomnio"], key="trastorno")



# Crear lista de resultados
resultados = []
# resultados = []  # Inicialización

# Botón de predicción
if st.button("Predecir con todos los modelos"):
    # Crear DataFrame con los datos ingresados
    input_data = pd.DataFrame({
        "Género": [genero],
        "Edad": [edad],
        "Ocupación": [ocupacion],

        "Duración del sueño": [dur_suenio],
        "Calidad del sueño": [cal_suenio],

        "Nivel de actividad física": [actividad],
        "Nivel de estrés": [estres],
        "Categoría de IMC": [imc],
        "Presión arterial": [presion],
        "Frecuencia cardíaca": [fc],
        "Pasos diarios": [pasos]
        # "Trastorno del sueño": [trastorno]
    })

    # Procesar cada modelo y mostrar resultados
    st.subheader("Resultados de la predicción")
    st.write(f"Hola {nombre_u}, estas son tus predicciones:")

    for nombre, modelo in modelos.items():
        pred = modelo.predict(input_data)
        resultados.append({
            "Modelo": nombre,
            "Trastorno del sueño": f"{pred[0]}" # pred[0]
        })

    # Convertir a DataFrame
df_resultados = pd.DataFrame(resultados)


# Generar tabla HTML con estilo
tabla_html = df_resultados.to_html(index=False, classes="styled-table")

# CSS para mejorar la presentación
css = """
<style>
.styled-table {
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 16px;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 10px rgba(0,0,0,0.15);
    border: 1px solid #cccccc; /* Bordes claros */
}
.styled-table thead tr {
    background-color: #009879;
    color: #ffffff; /* Texto blanco sobre fondo verde */
    text-align: center;
}
.styled-table th, .styled-table td {
    padding: 12px 15px;
    text-align: center;
    border: 1px solid #cccccc; /* Bordes claros en celdas */
    color: #dddddd; /* Fuente clara */
}
.styled-table tbody tr {
    border-bottom: 1px solid #cccccc; /* Bordes claros */
    color: #dddddd; /* Texto claro sobre fondo blanco */
}
.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
}
</style>
"""


# Mostrar tabla con estilo
st.markdown(css + tabla_html, unsafe_allow_html=True)

# Botón para resetear valores
if st.button("Resetear valores"):
    # st.rerun()
    st.session_state.clear()
    # st.experimental_rerun()
    reset_values()
    