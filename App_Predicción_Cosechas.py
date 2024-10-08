import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo entrenado
modelo = joblib.load('Modelo_Prediccion_Cosechas.pkl')

# Función para predicción usando el modelo cargado
def predecir_cosechas(input_data):
    input_df = pd.DataFrame([input_data])  # Convertir entrada a dataframe
    predicciones = modelo.predict(input_df)
    return predicciones

# Título de la aplicación
st.title("Predicción de Cosechas en Poza")

# Crear un diccionario para los inputs
input_usuario = {}

# Sección 1: Datos Particulares de Poza
st.header("Datos Particulares de Poza")

# Infraestructura (solo informativa, no usada para predicción)
infraestructura = st.text_input("Infraestructura")
input_usuario['Infraestructura'] = infraestructura  # Guardar, aunque no se usará en el modelo

# Área de Poza (Medida_Area_Infraestructura)
medida_area = st.number_input("Área de Poza", min_value=0.0)
input_usuario['Medida_Area_Infraestructura'] = medida_area

# Sección 2: Valores Medidos en Poza Durante Período entre Cosechas
st.header("Valores Medidos en Poza Durante Período entre Cosechas")

input_usuario['Promedio_K_Periodo'] = st.number_input("Promedio de K en Período")
input_usuario['Promedio_Na_Periodo'] = st.number_input("Promedio de Na en Período")
input_usuario['Promedio_Mg_Periodo'] = st.number_input("Promedio de Mg en Período")
input_usuario['Promedio_Ca_Periodo'] = st.number_input("Promedio de Ca en Período")
input_usuario['Promedio_SO4_Periodo'] = st.number_input("Promedio de SO4 en Período")
input_usuario['Promedio_Li_Periodo'] = st.number_input("Promedio de Li en Período")
input_usuario['Promedio_Cl_Periodo'] = st.number_input("Promedio de Cl en Período")
input_usuario['Promedio_H3BO3_Periodo'] = st.number_input("Promedio de H3BO3 en Período")

# Sección 3: Últimos Valores Medidos en Poza Previos a Cosecha
st.header("Últimos Valores Medidos en Poza Previos a Cosecha")

input_usuario['Último_Valor_K'] = st.number_input("Último Valor de K")
input_usuario['Último_Valor_Na'] = st.number_input("Último Valor de Na")
input_usuario['Último_Valor_Mg'] = st.number_input("Último Valor de Mg")
input_usuario['Último_Valor_Ca'] = st.number_input("Último Valor de Ca")
input_usuario['Último_Valor_SO4'] = st.number_input("Último Valor de SO4")
input_usuario['Último_Valor_Li'] = st.number_input("Último Valor de Li")
input_usuario['Último_Valor_Cl'] = st.number_input("Último Valor de Cl")
input_usuario['Último_Valor_H3BO3'] = st.number_input("Último Valor de H3BO3")

# Sección 4: Valores de Traspasos de Entrada a Poza Durante Período entre Cosechas
st.header("Valores de Traspasos de Entrada a Poza Durante Período entre Cosechas")

input_usuario['SUM_Ent_Traspaso'] = st.number_input("Volumen de Traspaso Total")
input_usuario['Promedio_Ent_Ponderado_K'] = st.number_input("Valor K Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_Na'] = st.number_input("Valor Na Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_Mg'] = st.number_input("Valor Mg Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_Ca'] = st.number_input("Valor Ca Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_SO4'] = st.number_input("Valor SO4 Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_Li'] = st.number_input("Valor Li Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_Cl'] = st.number_input("Valor Cl Traspaso Entrada")
input_usuario['Promedio_Ent_Ponderado_H3BO3'] = st.number_input("Valor H3BO3 Traspaso Entrada")

# Botón para hacer la predicción
if st.button("Predecir Cosechas y Sálidas"):
    predicciones = predecir_cosechas(input_usuario)
    st.subheader("Resultados de la Predicción:")
    st.write(f"Predicción: {predicciones}")

