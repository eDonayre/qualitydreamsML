import streamlit as st

# Definir las páginas apuntando a tus archivos .py
pg = st.navigation([
    st.Page("Prediccion03.py", title="Modelo Regresion", icon="📋"),
    st.Page("Prediccion04_Clasificacion.py", title="Modelo Clasificacion", icon="🌙")
])

# Configuración opcional de la página (título de la pestaña)
st.set_page_config(page_title="Mi App Machine Learning", layout="wide")

# Ejecutar la navegación
pg.run()