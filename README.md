# Análisis de Datos de Alura Store

Este documento describe dos scripts de Python utilizados para analizar datos de ventas y rendimiento de cuatro tiendas de Alura Store. El objetivo principal es proporcionar información valiosa para la toma de decisiones comerciales, en particular, para determinar qué tienda podría ser menos eficiente y, por lo tanto, un buen candidato para la venta.

## Requisitos del Sistema

* **Python 3.6 o superior**
* **pip** (el gestor de paquetes de Python, generalmente incluido con Python)

## Librerías Requeridas

Los scripts de Python utilizan las siguientes bibliotecas:

* `pandas` (para manipulación y análisis de datos)
* `matplotlib` (para visualización de datos - solo en el script de visualización)

## Instalación de Librerías

Para instalar las bibliotecas necesarias, sigue estos pasos:

1.  Abre tu terminal o línea de comandos.
2.  Asegúrate de que Python esté correctamente instalado. Puedes verificarlo ejecutando:

    ```bash
    python --version
    ```

3.  Instala `pandas`:

    ```bash
    pip install pandas
    ```

4.  Si vas a ejecutar el script de visualización, instala `matplotlib`:

    ```bash
    pip install matplotlib
    ```

## Código 1: Análisis Consolidado de Datos (`analisis_consolidado.py`)

Este script realiza un análisis completo de los datos de las tiendas, calculando varias métricas clave.

### Descripción del Código

El script realiza los siguientes análisis:

1.  **Carga de Datos:**
    * Carga los datos de cada tienda desde archivos CSV utilizando la biblioteca `pandas`.
    * Los datos se cargan en DataFrames de pandas (`tienda1_df`, `tienda2_df`, `tienda3_df`, `tienda4_df`).

2.  **Análisis de Ingresos:**
    * Calcula el ingreso total para cada tienda sumando los precios de los productos.
    * Crea un DataFrame (`ingresos_totales_df`) para comparar los ingresos totales entre las tiendas.

3.  **Análisis de Categorías Más Vendidas:**
    * Calcula los ingresos por categoría de producto para cada tienda.
    * Identifica las 3 categorías principales que generan más ingresos en cada tienda.
    * Crea DataFrames (`top_categorias_tienda1_df`, etc.) para mostrar las categorías principales.

4.  **Análisis de Reseñas de los Clientes:**
    * Calcula la calificación promedio de los clientes para cada tienda.
    * Crea un DataFrame (`calificaciones_promedio_df`) para comparar las calificaciones promedio.

5.  **Análisis de Productos Más Vendidos:**
    * Calcula los ingresos generados por cada producto en cada tienda.
    * Identifica los 5 productos principales que generan más ingresos.
    * Crea DataFrames (`top_productos_tienda1_df`, etc.) para mostrar los productos principales.

6.  **Análisis del Envío Promedio:**
    * Calcula el costo de envío promedio para cada tienda.
    * Crea un DataFrame (`costos_envio_promedio_df`) para comparar los costos de envío promedio.

7.  **Impresión de Resultados:**
    * Imprime todos los resultados de los análisis en la consola, organizados por sección.

### Uso

1.  Asegúrate de tener Python y `pandas` instalados.
2.  Coloca el script (`analisis_consolidado.py`) y los archivos CSV de las tiendas en el mismo directorio (o ajusta las rutas en el script).
3.  Ejecuta el script desde la terminal:

    ```bash
    python analisis_consolidado.py
    ```

## Código 2: Visualización de Datos (`visualizacion_datos.py`)

Este script genera visualizaciones de los datos de las tiendas para facilitar la comprensión de los resultados del análisis.

### Descripción del Código

El script realiza los siguientes análisis y visualizaciones:

1.  **Carga de Datos:**
    * Similar al script anterior, carga los datos de las tiendas en DataFrames de pandas.

2.  **Análisis de Ingresos:**
    * Calcula el ingreso total para cada tienda.
    * Crea un DataFrame (`ingresos_totales_df`) para los datos de ingresos.

3.  **Análisis de Reseñas de los Clientes:**
    * Calcula la calificación promedio para cada tienda.
    * Crea un DataFrame (`calificaciones_promedio_df`) para los datos de calificaciones.

4.  **Visualizaciones:**
    * **Gráfico de Barras: Ingresos Totales por Tienda:**
        * Crea un gráfico de barras para comparar los ingresos totales entre las tiendas.
    * **Gráfico de Barras: Calificación Promedio por Tienda:**
        * Crea un gráfico de barras para comparar las calificaciones promedio entre las tiendas.
    * **Gráfico Circular: Distribución de Ingresos por Tienda:**
        * Crea un gráfico circular para mostrar la distribución porcentual de los ingresos totales entre las tiendas.

### Uso

1.  Asegúrate de tener Python, `pandas` y `matplotlib` instalados.
2.  Coloca el script (`visualizacion_datos.py`) y los archivos CSV de las tiendas en el mismo directorio (o ajusta las rutas en el script).
3.  Ejecuta el script desde la terminal:

    ```bash
    python visualizacion_datos.py
    ```

## Recomendación de Venta (`recomendacion.md`)

Además de los scripts, se proporciona una recomendación en formato Markdown sobre qué tienda vender.

### Contenido de la Recomendación

El archivo Markdown contiene:

* **Análisis Realizado:** Una descripción del análisis realizado (ingresos totales y calificaciones promedio).
* **Recomendación:** La recomendación de vender la Tienda 4.
* **Justificación Basada en los Datos:** La justificación de la recomendación, basada en los ingresos totales y las calificaciones promedio.
* **Implicaciones para el Sr. João:** Las implicaciones de la venta para el propietario del negocio.
* **Limitaciones:** Las limitaciones del análisis (por ejemplo, no considerar costos operativos).
* **Conclusión:** Una conclusión que reafirma la recomendación.

## Estructura de Datos

Los conjuntos de datos de las tiendas contienen la siguiente información:

* **Producto y Categoría:** Artículos vendidos y sus categorías.
* **Precio y Envío:** Valores de venta y costos asociados.
* **Fecha y Lugar de Compra:** Información temporal y geográfica.
* **Evaluación de Compra:** Comentarios de clientes (calificaciones).
* **Tipo de Pago y Cuotas:** Métodos de pago utilizados.
* **Coordenadas Geográficas:** Ubicación de las transacciones (latitud y longitud).

## Conclusión

Estos scripts y la recomendación proporcionan un marco completo para analizar los datos de Alura Store y tomar decisiones informadas sobre la venta de una tienda. Los scripts están diseñados para ser claros, modulares y fáciles de entender, lo que facilita su mantenimiento y adaptación a futuras necesidades.