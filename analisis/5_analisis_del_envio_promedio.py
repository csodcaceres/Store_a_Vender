import pandas as pd

#-------------------------------------------------------------------------------------------
# ----- 1. Cargar de datos para analisis
#-------------------------------------------------------------------------------------------
url_tienda1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_tienda2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_tienda3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_tienda4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1_df = pd.read_csv(url_tienda1)
tienda2_df = pd.read_csv(url_tienda2)
tienda3_df = pd.read_csv(url_tienda3)
tienda4_df = pd.read_csv(url_tienda4)

#-------------------------------------------------------------------------------------------
# --- 2. Calcular el costo de envío promedio
#-------------------------------------------------------------------------------------------
costo_envio_promedio_tienda1 = tienda1_df['Costo de envío'].mean()
costo_envio_promedio_tienda2 = tienda2_df['Costo de envío'].mean()
costo_envio_promedio_tienda3 = tienda3_df['Costo de envío'].mean()
costo_envio_promedio_tienda4 = tienda4_df['Costo de envío'].mean()

#-------------------------------------------------------------------------------------------
# --- 3. DataFrame para comparar los costos de envío promedio
#-------------------------------------------------------------------------------------------
costos_envio_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Costo de Envío Promedio': [
        costo_envio_promedio_tienda1,
        costo_envio_promedio_tienda2,
        costo_envio_promedio_tienda3,
        costo_envio_promedio_tienda4
    ]
})

#-------------------------------------------------------------------------------------------
# --- 4. Imprimir los resultados
#-------------------------------------------------------------------------------------------
print("\n--- Costo de Envío Promedio por Tienda ---")
print(costos_envio_promedio_df)

# --- 3. Asumir que 'Fecha de Compra' es la fecha de envío (misma limitación que antes) ---
# --- 4. Calcular el envío promedio (en días) para cada tienda (sigue siendo ilustrativo) ---
# (Código ilustrativo - NO FUNCIONARÁ con los datos proporcionados)
# Si tuviéramos una columna 'Fecha de Entrega' (también en formato datetime):
# envio_promedio_tienda1 = (tienda1_df['Fecha de Entrega'] - tienda1_df['Fecha de Compra']).mean().days
# envio_promedio_tienda2 = (tienda2_df['Fecha de Entrega'] - tienda2_df['Fecha de Compra']).mean().days
# envio_promedio_tienda3 = (tienda3_df['Fecha de Entrega'] - tienda3_df['Fecha de Compra']).mean().days
# envio_promedio_tienda4 = (tienda4_df['Fecha de Entrega'] - tienda4_df['Fecha de Compra']).mean().days

# --- 5. Imprimir un mensaje informativo ---
print("\nAnálisis del Envío Promedio:")
print("\nNo se puede calcular el envío promedio con los datos proporcionados.")
print("Se requiere la 'Fecha de Entrega' para realizar este análisis.")
print("\nSin embargo, se corrigió la conversión de la 'Fecha de Compra' al formato datetime.")