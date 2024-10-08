import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
modelo = joblib.load("Modelo_Prediccion_Cosechas.pkl")

# Función para procesar las entradas del usuario
def procesar_datos_entrada(input_usuario):
    # Convertir a DataFrame
    input_df = pd.DataFrame([input_usuario])

    # Asegurar que las columnas estén en el mismo orden que durante el entrenamiento del modelo
    columnas_modelo = ['Último_Valor_K', 'Último_Valor_Na', 'Último_Valor_Mg', 'Último_Valor_Ca', 'Último_Valor_SO4', 
                       'Último_Valor_Li', 'Último_Valor_Cl', 'Último_Valor_H3BO3', 'Promedio_K_Periodo', 
                       'Promedio_Na_Periodo', 'Promedio_Mg_Periodo', 'Promedio_Ca_Periodo', 'Promedio_SO4_Periodo', 
                       'Promedio_Li_Periodo', 'Promedio_Cl_Periodo', 'Promedio_H3BO3_Periodo', 'SUM_Ent_Traspaso', 
                       'Promedio_Ent_Ponderado_K', 'Promedio_Ent_Ponderado_Na', 'Promedio_Ent_Ponderado_Mg', 
                       'Promedio_Ent_Ponderado_Ca', 'Promedio_Ent_Ponderado_SO4', 'Promedio_Ent_Ponderado_Li', 
                       'Promedio_Ent_Ponderado_Cl', 'Promedio_Ent_Ponderado_H3BO3', 'Medida_Area_Infraestructura']
    
    # Asegurarse de que las columnas están en el orden correcto
    input_df = input_df[columnas_modelo]

    # Asegurar que todas las columnas sean de tipo float
    input_df = input_df.astype(float)

    # Reemplazar valores NaN o None con ceros
    input_df = input_df.fillna(0)

    return input_df

# Título de la app
st.title("Predicción de Cosechas en Poza")

# Sección 1: Datos Particulares de Poza
st.header("Datos Particulares de Poza")
infraestructura = st.text_input("Infraestructura")
area_poza = st.number_input("Área de Poza", min_value=0.0)

# Sección 2: Valores Medidos en Poza Durante Período entre Cosechas
st.header("Valores Medidos en Poza Durante Período entre Cosechas")
promedio_k_periodo = st.number_input("Promedio de K en Período", value=0.0)
promedio_na_periodo = st.number_input("Promedio de Na en Período", value=0.0)
promedio_mg_periodo = st.number_input("Promedio de Mg en Período", value=0.0)
promedio_ca_periodo = st.number_input("Promedio de Ca en Período", value=0.0)
promedio_so4_periodo = st.number_input("Promedio de SO4 en Período", value=0.0)
promedio_li_periodo = st.number_input("Promedio de Li en Período", value=0.0)
promedio_cl_periodo = st.number_input("Promedio de Cl en Período", value=0.0)
promedio_h3bo3_periodo = st.number_input("Promedio de H3BO3 en Período", value=0.0)

# Sección 3: Últimos Valores Medidos en Poza Previos a Cosecha
st.header("Últimos Valores Medidos en Poza Previos a Cosecha")
ultimo_valor_k = st.number_input("Último Valor de K", value=0.0)
ultimo_valor_na = st.number_input("Último Valor de Na", value=0.0)
ultimo_valor_mg = st.number_input("Último Valor de Mg", value=0.0)
ultimo_valor_ca = st.number_input("Último Valor de Ca", value=0.0)
ultimo_valor_so4 = st.number_input("Último Valor de SO4", value=0.0)
ultimo_valor_li = st.number_input("Último Valor de Li", value=0.0)
ultimo_valor_cl = st.number_input("Último Valor de Cl", value=0.0)
ultimo_valor_h3bo3 = st.number_input("Último Valor de H3BO3", value=0.0)

# Sección 4: Valores de Traspasos de Entrada a Poza Durante Período entre Cosechas
st.header("Valores de Traspasos de Entrada a Poza Durante Período entre Cosechas")
volumen_traspaso_total = st.number_input("Volumen de Traspaso Total", value=0.0)
valor_k_traspaso_entrada = st.number_input("Valor K Traspaso Entrada", value=0.0)
valor_na_traspaso_entrada = st.number_input("Valor Na Traspaso Entrada", value=0.0)
valor_mg_traspaso_entrada = st.number_input("Valor Mg Traspaso Entrada", value=0.0)
valor_ca_traspaso_entrada = st.number_input("Valor Ca Traspaso Entrada", value=0.0)
valor_so4_traspaso_entrada = st.number_input("Valor SO4 Traspaso Entrada", value=0.0)
valor_li_traspaso_entrada = st.number_input("Valor Li Traspaso Entrada", value=0.0)
valor_cl_traspaso_entrada = st.number_input("Valor Cl Traspaso Entrada", value=0.0)
valor_h3bo3_traspaso_entrada = st.number_input("Valor H3BO3 Traspaso Entrada", value=0.0)

# Diccionario con los valores introducidos
input_usuario = {
    "Medida_Area_Infraestructura": area_poza,
    "Promedio_K_Periodo": promedio_k_periodo,
    "Promedio_Na_Periodo": promedio_na_periodo,
    "Promedio_Mg_Periodo": promedio_mg_periodo,
    "Promedio_Ca_Periodo": promedio_ca_periodo,
    "Promedio_SO4_Periodo": promedio_so4_periodo,
    "Promedio_Li_Periodo": promedio_li_periodo,
    "Promedio_Cl_Periodo": promedio_cl_periodo,
    "Promedio_H3BO3_Periodo": promedio_h3bo3_periodo,
    "Último_Valor_K": ultimo_valor_k,
    "Último_Valor_Na": ultimo_valor_na,
    "Último_Valor_Mg": ultimo_valor_mg,
    "Último_Valor_Ca": ultimo_valor_ca,
    "Último_Valor_SO4": ultimo_valor_so4,
    "Último_Valor_Li": ultimo_valor_li,
    "Último_Valor_Cl": ultimo_valor_cl,
    "Último_Valor_H3BO3": ultimo_valor_h3bo3,
    "SUM_Ent_Traspaso": volumen_traspaso_total,
    "Promedio_Ent_Ponderado_K": valor_k_traspaso_entrada,
    "Promedio_Ent_Ponderado_Na": valor_na_traspaso_entrada,
    "Promedio_Ent_Ponderado_Mg": valor_mg_traspaso_entrada,
    "Promedio_Ent_Ponderado_Ca": valor_ca_traspaso_entrada,
    "Promedio_Ent_Ponderado_SO4": valor_so4_traspaso_entrada,
    "Promedio_Ent_Ponderado_Li": valor_li_traspaso_entrada,
    "Promedio_Ent_Ponderado_Cl": valor_cl_traspaso_entrada,
    "Promedio_Ent_Ponderado_H3BO3": valor_h3bo3_traspaso_entrada,
}

# Procesar los datos de entrada
input_df = procesar_datos_entrada(input_usuario)

# Realizar la predicción
if st.button("Predecir"):
    try:
        predicciones = modelo.predict(input_df)
        st.write(f"Predicciones: {predicciones}")
    except Exception as e:
        st.error(f"Error en la predicción: {str(e)}")
