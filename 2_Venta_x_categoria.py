import pandas as pd

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
# ----- 1. Calcular los ingresos por categoría para cada tienda
# ----- Agrupamos datos por 'Categoría del Producto' y sumamos los 'Precio' por cada tienda
#-------------------------------------------------------------------------------------------
ingresos_por_categoria_tienda1 = tienda1_df.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda2 = tienda2_df.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda3 = tienda3_df.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda4 = tienda4_df.groupby('Categoría del Producto')['Precio'].sum()

#-------------------------------------------------------------------------------------------
# --- 2. Crear un DataFrame de comparación
# Creamos un DataFrame para comparar los ingresos por categoría entre las tiendas
# Reemplazamos los valores NaN con 0
#-------------------------------------------------------------------------------------------
ingresos_por_categoria_df = pd.DataFrame({
    'Tienda 1': ingresos_por_categoria_tienda1,
    'Tienda 2': ingresos_por_categoria_tienda2,
    'Tienda 3': ingresos_por_categoria_tienda3,
    'Tienda 4': ingresos_por_categoria_tienda4
}).fillna(0)  

#-------------------------------------------------------------------------------------------
# ----- 3. Encontrar las 3 categorías principales para cada tienda
# ----- Definimos cuántas categorías vamos a trabajar
#-------------------------------------------------------------------------------------------
num_total_categorias = 3  
categorias_tienda1 = ingresos_por_categoria_tienda1.nlargest(num_total_categorias)
categorias_tienda2 = ingresos_por_categoria_tienda2.nlargest(num_total_categorias)
categorias_tienda3 = ingresos_por_categoria_tienda3.nlargest(num_total_categorias)
categorias_tienda4 = ingresos_por_categoria_tienda4.nlargest(num_total_categorias)

#-------------------------------------------------------------------------------------------
# ----- 4. DataFrames para las 3 categorías principales de cada tienda
#-------------------------------------------------------------------------------------------
principal_categorias_tienda1_df = pd.DataFrame({'Categoría': categorias_tienda1.index, 'Ingresos': categorias_tienda1.values})
principal_categorias_tienda2_df = pd.DataFrame({'Categoría': categorias_tienda2.index, 'Ingresos': categorias_tienda2.values})
principal_categorias_tienda3_df = pd.DataFrame({'Categoría': categorias_tienda3.index, 'Ingresos': categorias_tienda3.values})
principal_categorias_tienda4_df = pd.DataFrame({'Categoría': categorias_tienda4.index, 'Ingresos': categorias_tienda4.values})

#-------------------------------------------------------------------------------------------
# --- 5. Imprimir los totales por pantalla
#-------------------------------------------------------------------------------------------
print("Ingresos de Categorías Más Vendidas por cada tienda:")
print("\nIngresos por Categoría (Comparación totales de producto entre Tiendas):\n", ingresos_por_categoria_df)

print("\n -", "Categorías mas vendidas - Tienda 1:\n", principal_categorias_tienda1_df)
print("\n -", "Categorías mas vendidas - Tienda 2:\n", principal_categorias_tienda2_df)
print("\n -", "Categorías mas vendidas - Tienda 3:\n", principal_categorias_tienda3_df)
print("\n -", "Categorías mas vendidas - Tienda 4:\n", principal_categorias_tienda4_df)

