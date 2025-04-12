import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

# --- 2. Análisis de Ingresos ---
ingreso_tienda1 = tienda['Precio'].sum()
ingreso_tienda2 = tienda2['Precio'].sum()
ingreso_tienda3 = tienda3['Precio'].sum()
ingreso_tienda4 = tienda4['Precio'].sum()

ingresos_totales_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Ingreso Total': [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
})

# --- 3. Análisis de Categorías Más Vendidas ---
ingresos_por_categoria_tienda1 = tienda.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda2 = tienda2.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda3 = tienda3.groupby('Categoría del Producto')['Precio'].sum()
ingresos_por_categoria_tienda4 = tienda4.groupby('Categoría del Producto')['Precio'].sum()

ingresos_por_categoria_df = pd.DataFrame({
    'Tienda 1': ingresos_por_categoria_tienda1,
    'Tienda 2': ingresos_por_categoria_tienda2,
    'Tienda 3': ingresos_por_categoria_tienda3,
    'Tienda 4': ingresos_por_categoria_tienda4
}).fillna(0)

num_top_categorias = 3
top_categorias_tienda1 = ingresos_por_categoria_tienda1.nlargest(num_top_categorias)
top_categorias_tienda2 = ingresos_por_categoria_tienda2.nlargest(num_top_categorias)
top_categorias_tienda3 = ingresos_por_categoria_tienda3.nlargest(num_top_categorias)
top_categorias_tienda4 = ingresos_por_categoria_tienda4.nlargest(num_top_categorias)

top_categorias_tienda1_df = pd.DataFrame({'Categoría': top_categorias_tienda1.index, 'Ingresos': top_categorias_tienda1.values})
top_categorias_tienda2_df = pd.DataFrame({'Categoría': top_categorias_tienda2.index, 'Ingresos': top_categorias_tienda2.values})
top_categorias_tienda3_df = pd.DataFrame({'Categoría': top_categorias_tienda3.index, 'Ingresos': top_categorias_tienda3.values})
top_categorias_tienda4_df = pd.DataFrame({'Categoría': top_categorias_tienda4.index, 'Ingresos': top_categorias_tienda4.values})

# --- 4. Análisis de Reseñas de los Clientes ---
calificacion_promedio_tienda1 = tienda['Calificación'].mean()
calificacion_promedio_tienda2 = tienda2['Calificación'].mean()
calificacion_promedio_tienda3 = tienda3['Calificación'].mean()
calificacion_promedio_tienda4 = tienda4['Calificación'].mean()

calificaciones_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Calificación Promedio': [calificacion_promedio_tienda1,
                               calificacion_promedio_tienda2,
                               calificacion_promedio_tienda3,
                               calificacion_promedio_tienda4]
})

# --- 5. Análisis de Productos Más Vendidos ---
ingresos_por_producto_tienda1 = tienda.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda2 = tienda2.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda3 = tienda3.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda4 = tienda4.groupby('Producto')['Precio'].sum()

num_top_productos = 5
top_productos_tienda1 = ingresos_por_producto_tienda1.nlargest(num_top_productos)
top_productos_tienda2 = ingresos_por_producto_tienda2.nlargest(num_top_productos)
top_productos_tienda3 = ingresos_por_producto_tienda3.nlargest(num_top_productos)
top_productos_tienda4 = ingresos_por_producto_tienda4.nlargest(num_top_productos)

top_productos_tienda1_df = pd.DataFrame({'Producto': top_productos_tienda1.index, 'Ingresos': top_productos_tienda1.values})
top_productos_tienda2_df = pd.DataFrame({'Producto': top_productos_tienda2.index, 'Ingresos': top_productos_tienda2.values})
top_productos_tienda3_df = pd.DataFrame({'Producto': top_productos_tienda3.index, 'Ingresos': top_productos_tienda3.values})
top_productos_tienda4_df = pd.DataFrame({'Producto': top_productos_tienda4.index, 'Ingresos': top_productos_tienda4.values})

# --- 6. Análisis del Envío Promedio ---
costo_envio_promedio_tienda1 = tienda['Costo de envío'].mean()
costo_envio_promedio_tienda2 = tienda2['Costo de envío'].mean()
costo_envio_promedio_tienda3 = tienda3['Costo de envío'].mean()
costo_envio_promedio_tienda4 = tienda4['Costo de envío'].mean()

costos_envio_promedio_df = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Costo de Envío Promedio': [
        costo_envio_promedio_tienda1,
        costo_envio_promedio_tienda2,
        costo_envio_promedio_tienda3,
        costo_envio_promedio_tienda4
    ]
})

# --- 7. Imprimir todos los resultados ---
print("\n--- Análisis Consolidado de Alura Store ---")

print("\n1. Análisis de Ingresos:")
print(ingresos_totales_df)

print("\n2. Análisis de Categorías Más Vendidas:")
print("\nIngresos por Categoría (Comparación entre Tiendas):\n", ingresos_por_categoria_df)
print("\nTop 3 Categorías - Tienda 1:\n", top_categorias_tienda1_df)
print("\nTop 3 Categorías - Tienda 2:\n", top_categorias_tienda2_df)
print("\nTop 3 Categorías - Tienda 3:\n", top_categorias_tienda3_df)
print("\nTop 3 Categorías - Tienda 4:\n", top_categorias_tienda4_df)

print("\n3. Análisis de Reseñas de Clientes:")
print("\nCalificación Promedio por Tienda:\n", calificaciones_promedio_df)

print("\n4. Análisis de Productos Más Vendidos (por Ingresos):")
print("\nTop 5 Productos - Tienda 1:\n", top_productos_tienda1_df)
print("\nTop 5 Productos - Tienda 2:\n", top_productos_tienda2_df)
print("\nTop 5 Productos - Tienda 3:\n", top_productos_tienda3_df)
print("\nTop 5 Productos - Tienda 4:\n", top_productos_tienda4_df)

print("\n5. Análisis del Envío Promedio:")
print(costos_envio_promedio_df)