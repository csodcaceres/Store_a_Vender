import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Cargar los datos ---
# Cargamos los datos de cada tienda desde las URLs proporcionadas
url_tienda1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_tienda2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_tienda3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_tienda4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1_df = pd.read_csv(url_tienda1)
tienda2_df = pd.read_csv(url_tienda2)
tienda3_df = pd.read_csv(url_tienda3)
tienda4_df = pd.read_csv(url_tienda4)

# --- 2. Calcular los ingresos totales ---
# Para calcular los ingresos totales de cada tienda, sumamos la columna 'Precio'
# Asumimos que la columna 'Precio' representa el precio de venta de cada producto
ingreso_tienda1 = tienda1_df['Precio'].sum()
ingreso_tienda2 = tienda2_df['Precio'].sum()
ingreso_tienda3 = tienda3_df['Precio'].sum()
ingreso_tienda4 = tienda4_df['Precio'].sum()

# --- 3. Crear un DataFrame de comparación ---
# Creamos un DataFrame para organizar los ingresos totales de cada tienda
ingresos_totales_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Ingreso Total': [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
})

# --- 4. Visualizar los ingresos totales ---
# Utilizamos un gráfico de barras para comparar visualmente los ingresos
plt.figure(figsize=(8, 6))  # Establecemos el tamaño de la figura
plt.bar(ingresos_totales_df['Tienda'], ingresos_totales_df['Ingreso Total'])  # Creamos las barras
plt.xlabel('Tienda')  # Etiquetamos el eje x
plt.ylabel('Ingreso Total')  # Etiquetamos el eje y
plt.title('Ingreso Total por Tienda')  # Añadimos un título al gráfico
plt.xticks(rotation=45, ha="right")  # Rotamos las etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustamos el diseño para evitar que las etiquetas se superpongan
plt.show()  # Mostramos el gráfico

# --- 5. Imprimir los resultados ---
print("Análisis de Ingresos Totales:")
print(ingresos_totales_df)