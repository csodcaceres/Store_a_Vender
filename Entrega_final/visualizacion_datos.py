import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Cargar los datos ---
url_tienda1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_tienda2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_tienda3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_tienda4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1_df = pd.read_csv(url_tienda1)
tienda2_df = pd.read_csv(url_tienda2)
tienda3_df = pd.read_csv(url_tienda3)
tienda4_df = pd.read_csv(url_tienda4)

# --- 2. Análisis de Ingresos (Reutilizando el código anterior) ---
ingreso_tienda1 = tienda1_df['Precio'].sum()
ingreso_tienda2 = tienda2_df['Precio'].sum()
ingreso_tienda3 = tienda3_df['Precio'].sum()
ingreso_tienda4 = tienda4_df['Precio'].sum()

ingresos_totales_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Ingreso Total': [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
})

# --- 3. Análisis de Reseñas de los Clientes (Reutilizando el código anterior) ---
calificacion_promedio_tienda1 = tienda1_df['Calificación'].mean()
calificacion_promedio_tienda2 = tienda2_df['Calificación'].mean()
calificacion_promedio_tienda3 = tienda3_df['Calificación'].mean()
calificacion_promedio_tienda4 = tienda4_df['Calificación'].mean()

calificaciones_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Calificación Promedio': [calificacion_promedio_tienda1,
                               calificacion_promedio_tienda2,
                               calificacion_promedio_tienda3,
                               calificacion_promedio_tienda4]
})

# --- 4. Visualizaciones ---

# 4.1. Gráfico de Barras: Ingresos Totales por Tienda
plt.figure(figsize=(8, 6))
plt.bar(ingresos_totales_df['Tienda'], ingresos_totales_df['Ingreso Total'], color='skyblue')
plt.xlabel('Tienda')
plt.ylabel('Ingreso Total')
plt.title('Ingreso Total por Tienda')
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 4.2. Gráfico de Barras: Calificación Promedio por Tienda
plt.figure(figsize=(8, 6))
plt.bar(calificaciones_promedio_df['Tienda'], calificaciones_promedio_df['Calificación Promedio'], color='lightgreen')
plt.xlabel('Tienda')
plt.ylabel('Calificación Promedio')
plt.title('Calificación Promedio por Tienda')
plt.xticks(rotation=45, ha="right")
plt.ylim(0, 5)  # Asumiendo una escala de calificación de 1 a 5
plt.tight_layout()
plt.show()

# 4.3. Gráfico Circular: Distribución de Ingresos por Tienda
plt.figure(figsize=(8, 8))
plt.pie(ingresos_totales_df['Ingreso Total'], labels=ingresos_totales_df['Tienda'], autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue', 'lightgreen', 'lightsalmon'])
plt.title('Distribución de Ingresos Totales por Tienda')
plt.tight_layout()
plt.show()