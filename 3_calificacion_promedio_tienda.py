import pandas as pd
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------
# ----- 1. Cargar de datos para analisis -----
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
# --- 1. Calcular la calificación promedio por tienda ---
#-------------------------------------------------------------------------------------------
calificacion_promedio_tienda1 = tienda1_df['Calificación'].mean()
calificacion_promedio_tienda2 = tienda2_df['Calificación'].mean()
calificacion_promedio_tienda3 = tienda3_df['Calificación'].mean()
calificacion_promedio_tienda4 = tienda4_df['Calificación'].mean()

#-------------------------------------------------------------------------------------------
# --- 2. Crear un DataFrame de comparación de calificaciones promedio ---
#-------------------------------------------------------------------------------------------
calificaciones_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Calificación Promedio': [calificacion_promedio_tienda1,
                               calificacion_promedio_tienda2,
                               calificacion_promedio_tienda3,
                               calificacion_promedio_tienda4]
})

#-------------------------------------------------------------------------------------------
# --- 3. Visualizar las calificaciones promedio ---
#-------------------------------------------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.bar(calificaciones_promedio_df['Tienda'], calificaciones_promedio_df['Calificación Promedio'], color='skyblue')
plt.xlabel('Tienda')
plt.ylabel('Calificación Promedio')
plt.title('Calificación Promedio por Tienda')
plt.xticks(rotation=45, ha="right")
# Asumimos que la calificación es en de 1 a 5
plt.ylim(0, 5)  
plt.tight_layout()
plt.show()

#-------------------------------------------------------------------------------------------
# --- 4. Analizar la distribución de las calificaciones ---
# Creamos histogramas para visualizar la distribución de las calificaciones en cada tienda
#-------------------------------------------------------------------------------------------
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)  # Subplot para la Tienda 1 (2 filas, 2 columnas, posición 1)
plt.hist(tienda1_df['Calificación'], bins=5, range=(1, 5), edgecolor='black', color='lightcoral')
plt.title('Distribución de Calificaciones - Tienda 1')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 2)  # Subplot para la Tienda 2 (2 filas, 2 columnas, posición 2)
plt.hist(tienda2_df['Calificación'], bins=5, range=(1, 5), edgecolor='black', color='lightgreen')
plt.title('Distribución de Calificaciones - Tienda 2')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 3)  # Subplot para la Tienda 3 (2 filas, 2 columnas, posición 3)
plt.hist(tienda3_df['Calificación'], bins=5, range=(1, 5), edgecolor='black', color='lightsalmon')
plt.title('Distribución de Calificaciones - Tienda 3')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')

plt.subplot(2, 2, 4)  # Subplot para la Tienda 4 (2 filas, 2 columnas, posición 4)
plt.hist(tienda4_df['Calificación'], bins=5, range=(1, 5), edgecolor='black', color='lightskyblue')
plt.title('Distribución de Calificaciones - Tienda 4')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

#-------------------------------------------------------------------------------------------
# --- 5. Imprimir los resultados ---
#-------------------------------------------------------------------------------------------
print("\nAnálisis de Reseñas de Clientes:")
print("\nCalificación Promedio por Tienda:\n", calificaciones_promedio_df)