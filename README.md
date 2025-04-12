# Bienvenidos Store_a_Vender

Durante este proyecto, ayudaremos al Sr. Juan a decidir qué tienda de su cadena Store debe vender para iniciar un nuevo emprendimiento. Para ello, analizarás datos de ventas, rendimiento y reseñas de las 4 tiendas de Store. El objetivo es identificar la tienda menos eficiente y presentar una recomendación final basada en los datos.

- Cargue y manipule datos CSV con la biblioteca Pandas.
- Cree visualizaciones de datos con la biblioteca Matplotlib.
- Analice métricas como ingresos, reseñas y rendimiento de ventas.

### Requisitos:

Analizar datos de la tienda:

Evaluar información como los ingresos, las categorías más vendidas, las reseñas de los clientes, los productos más vendidos y el envío promedio.

### Crear gráficos para visualización:

Decidir qué tipos de gráficos utilizar para presentar los resultados de forma clara y visual.

Mínimo de 3 gráficos diferentes, que pueden incluir gráficos de barras, circulares, de dispersión y otros.

### Enviar una recomendación:

Después del análisis, escriba un texto explicando a qué tienda debería vender el Sr. João y por qué, basándose en los datos presentados.

# 1: Análisis Consolidado de Datos (analisis_consolidado.py)
Este script analiza de forma integral los datos de las tiendas, calculando métricas clave para evaluar su rendimiento.

Carga de Datos:

- El script utiliza la biblioteca pandas para cargar los datos de cada tienda desde archivos CSV.
- Los datos de cada tienda se almacenan en DataFrames de pandas llamados: tienda1_df, tienda2_df,   tienda3_df y tienda4_df.

Análisis de Ingresos:

- El script calcula el ingreso total de cada tienda sumando los precios de los productos en sus respectivos DataFrames.
- Se crea un DataFrame llamado ingresos_totales_df para comparar los ingresos totales de las distintas tiendas de manera estructurada.

Análisis de Categorías Más Vendidas:

- El script también calcula los ingresos por categoría de producto en cada tienda, permitiendo un análisis más detallado del rendimiento por tipo de producto.
- El script identifica las 3 categorías con mayores ingresos en cada tienda y crea DataFrames como top_categorias_tienda1_df, top_categorias_tienda2_df, etc., para mostrar claramente estas categorías destacadas.

Análisis de Reseñas de los Clientes:

- El script calcula la calificación promedio de los clientes para cada tienda y crea un DataFrame llamado calificaciones_promedio_df para facilitar la comparación entre ellas.

Análisis de Productos Más Vendidos:

- Se calculan los ingresos por producto en cada tienda, se identifican los 5 productos con mayores ingresos y se crean DataFrames como top_productos_tienda1_df, top_productos_tienda2_df, etc., para mostrar estos productos destacados.

Análisis del Envío Promedio:

- Se calcula el costo de envío promedio para cada tienda y se crea un DataFrame llamado costos_envio_promedio_df para comparar estos costos entre las tiendas.

Impresión de Resultados:

- Se imprimen todos los resultados del análisis en la consola, organizados por sección. Esto incluye ingresos totales, calificaciones promedio, costos de envío, ingresos por categoría, principales categorías y productos, permitiendo una visualización clara y estructurada de la información.

Uso
- Asegúrate de tener Python y pandas instalados.

- Coloca el script (analisis_consolidado.py) y los archivos CSV de las tiendas en el mismo directorio (o ajusta las rutas en el script).

- Ejecuta el script desde la terminal:

python analisis_consolidado.py

Código 2: Visualización de Datos (visualizacion_datos.py)
Este script genera visualizaciones de los datos de las tiendas para facilitar la comprensión de los resultados del análisis.

Descripción del Código
El script realiza los siguientes análisis y visualizaciones:

Carga de Datos:

Similar al script anterior, carga los datos de las tiendas en DataFrames de pandas.
Análisis de Ingresos:

Calcula el ingreso total para cada tienda.
Crea un DataFrame (ingresos_totales_df) para los datos de ingresos.
Análisis de Reseñas de los Clientes:

Calcula la calificación promedio para cada tienda.
Crea un DataFrame (calificaciones_promedio_df) para los datos de calificaciones.
Visualizaciones:

Gráfico de Barras: Ingresos Totales por Tienda:
Crea un gráfico de barras para comparar los ingresos totales entre las tiendas.
Gráfico de Barras: Calificación Promedio por Tienda:
Crea un gráfico de barras para comparar las calificaciones promedio entre las tiendas.
Gráfico Circular: Distribución de Ingresos por Tienda:
Crea un gráfico circular para mostrar la distribución porcentual de los ingresos totales entre las tiendas.

### Uso
Asegúrate de tener Python, pandas y matplotlib instalados.

Coloca el script (visualizacion_datos.py) y los archivos CSV de las tiendas en el mismo directorio (o ajusta las rutas en el script).

Ejecuta el script desde la terminal:

    python visualizacion_datos.py

### Recomendación de Venta (recomendacion.md)

Además de los scripts, se proporciona una recomendación en formato Markdown sobre qué tienda vender.

Contenido de la Recomendación
El archivo Markdown contiene:

- Análisis Realizado: Una descripción del análisis realizado (ingresos totales y calificaciones promedio).
- Recomendación: La recomendación de vender la Tienda 4.
- Justificación Basada en los Datos: La justificación de la recomendación, basada en los ingresos totales y las calificaciones promedio.
- Implicaciones para el Sr. João: Las implicaciones de la venta para el propietario del negocio.
- Limitaciones: Las limitaciones del análisis (por ejemplo, no considerar costos operativos).
- Conclusión: Una conclusión que reafirma la recomendación.

Estructura de Datos
Los conjuntos de datos de las tiendas contienen la siguiente información:

- Producto y Categoría: Artículos vendidos y sus categorías.
- Precio y Envío: Valores de venta y costos asociados.
- Fecha y Lugar de Compra: Información temporal y geográfica.
- Evaluación de Compra: Comentarios de clientes (calificaciones).
- Tipo de Pago y Cuotas: Métodos de pago utilizados.
- Coordenadas Geográficas: Ubicación de las transacciones (latitud y longitud).

- Conclusión
Estos análisis y la recomendación ofrecen un marco integral para evaluar los datos de Alura Store y tomar decisiones informadas sobre la venta de una tienda. Las herramientas utilizadas son claras, modulares y fáciles de entender, lo que permite su mantenimiento y adaptación a futuras necesidades.