import streamlit as st
import pandas as pd
import joblib

# Función para procesar las entradas del usuario
def procesar_datos_entrada(input_usuario):
    # Convertir a DataFrame
    input_df = pd.DataFrame([input_usuario])

    # Asegurar que todas las columnas sean de tipo float
    input_df = input_df.astype(float)

    # Reemplazar valores NaN o None con ceros
    input_df = input_df.fillna(0)

    return input_df

# Título de la app
st.title("Predicción de Cosechas en Poza")

# Sección para seleccionar el modelo a usar
st.header("Seleccionar el modelo para la predicción")
modelos_disponibles = {
    "Modelo General de Predicción": "Modelo_Prediccion_Cosechas.pkl",
    "Modelo Específico 1": "Modelo_Prediccion_Cosechas_1.pkl",
    "Modelo Específico 2": "Modelo_Prediccion_Cosechas_2.pkl"
}

# Crear un menú desplegable para seleccionar el modelo
modelo_seleccionado = st.selectbox("Selecciona un modelo", list(modelos_disponibles.keys()))

# Cargar el modelo seleccionado
modelo = joblib.load(modelos_disponibles[modelo_seleccionado])

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
    "Medida_Area_Infraestructura": area_poza,  # Update name
    "Promedio_K_Periodo": promedio_k_periodo,
    "Promedio_Na_Periodo": promedio_na_periodo,  # Ensure correct spelling
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
    "SUM_Ent_Traspaso": volumen_traspaso_total,  # Correct name
    "Promedio_Ent_Ponderado_K": valor_k_traspaso_entrada,  # Correct name
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

# Predicciones por cada salida
salidas = ['Suma de TiempoOperacion', 'Cosecha_ton', 'SUM_Sal_Traspaso', 
           'Promedio_Sal_Ponderado_K', 'Promedio_Sal_Ponderado_Na', 
           'Promedio_Sal_Ponderado_Mg', 'Promedio_Sal_Ponderado_Ca', 
           'Promedio_Sal_Ponderado_SO4', 'Promedio_Sal_Ponderado_Li', 
           'Promedio_Sal_Ponderado_Cl', 'K_pct', 'Na_pct', 'Mg_pct', 
           'Ca_pct', 'SO4_pct', 'Li_pct', 'Cl_pct', 'H3BO3_pct']

# Realizar la predicción
if st.button("Predecir"):
    try:
        # Crear un diccionario para almacenar las predicciones
        predicciones = {}

        # Iterar sobre las salidas y realizar una predicción para cada columna
        for columna in salidas:
            # Realizar la predicción para cada columna de salida
            prediccion = modelo.predict(input_df)
            # Guardar la predicción en el diccionario
            predicciones[columna] = prediccion[0]  # Acceder al primer elemento de la predicción
        
        # Mostrar los resultados de las predicciones
        st.subheader("Predicciones:")
        for columna, prediccion in predicciones.items():
            st.write(f"{columna}: {prediccion}")

    except Exception as e:
        st.error(f"Error en la predicción: {str(e)}")