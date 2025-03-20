import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Dashboard de Anuncios de Venta de Coches",
    page_icon="🚗",
    layout="wide"
)

# Título principal
st.title("Dashboard de Anuncios de Venta de Coches")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar información básica
st.header("Información sobre los datos")
st.write(f"Este dataset contiene {car_data.shape[0]} anuncios de venta de coches con {car_data.shape[1]} variables.")

# Sidebar con opciones
st.sidebar.header("Opciones de visualización")

# Opción para mostrar datos crudos
if st.sidebar.checkbox("Mostrar datos crudos"):
    st.subheader("Datos crudos")
    st.write(car_data.head(50))

# Sección de visualizaciones
st.header("Visualizaciones")

# Opción 1: Histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.subheader("Histograma de lecturas del odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Opción 2: Gráfico de dispersión    
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.subheader("Relación entre el odómetro y el precio")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Alternativa con checkbox
st.header("Visualizaciones con checkbox")

if st.checkbox('Mostrar histograma de odómetro'):
    st.subheader("Histograma de lecturas del odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar relación odómetro/precio'):
    st.subheader("Relación entre el odómetro y el precio")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)