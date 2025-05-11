
# 📊 Descripción del Proyecto

Store_a_Vender es una aplicación diseñada para analizar los datos de ventas y rendimiento de cuatro tiendas de Alura Store. La aplicación permite realizar análisis detallados sobre las ventas, productos más vendidos, comparación de rendimiento entre tiendas y otras métricas clave. Está orientada a ayudar a los gerentes de las tiendas a tomar decisiones informadas para optimizar sus operaciones.

---

## ✅ Requisitos del Sistema

- **Python 3.6 o superior**
- **pip** (gestor de paquetes de Python)

---

## 📦 Librerías Necesarias

Los análisis requieren las siguientes bibliotecas:

- `pandas` → Manipulación y análisis de datos  
- `matplotlib` → Visualización de datos (solo para el script gráfico)

### Instalación de Librerías

```bash
pip install pandas
pip install matplotlib  # Solo si usarás la visualización
```

---

## 📁 Código 1: Análisis Consolidado de Datos (`analisis_consolidado.py`)

Este análisis realiza un estudio detallado sobre el rendimiento de cada tienda, incluyendo:

### 🔍 Qué Hace:

1. **Carga de Datos**
   - Lee los archivos `.csv` de cada tienda y los almacena en `DataFrames`:
     - `tienda1_df`, `tienda2_df`, `tienda3_df`, `tienda4_df`

2. **Ingresos Totales**
   - Suma los precios para calcular los ingresos por tienda
   - Se crea `ingresos_totales_df` para comparar resultados

3. **Categorías Más Rentables**
   - Calcula ingresos por categoría en cada tienda
   - Identifica las 3 categorías que más generan
   - Se crean `top_categorias_tienda_df` para visualización

4. **Calificación Promedio**
   - Calcula la media de calificaciones de los clientes por tienda
   - Se resume en `calificaciones_promedio_df`

5. **Productos Más Vendidos**
   - Suma ingresos por producto
   - Identifica los 5 productos más lucrativos
   - Se crean `top_productos_tienda_df` por tienda

6. **Costo de Envío Promedio**
   - Calcula el promedio del costo de envío por tienda
   - Se crea `costos_envio_promedio_df`

7. **Impresión de Resultados**
   - Todos los resultados se imprimen en consola organizados por sección

### ▶️ Cómo Ejecutarlo

1. Coloca el archivo `analisis_consolidado.py` y los `.csv` en el mismo directorio  
2. Ejecuta:

```bash
python analisis_consolidado.py
```

---

## 📊 Código 2: Visualización de Datos (`visualizacion_datos.py`)

Este archivo genera gráficas que ayudan a interpretar mejor los datos.

### 🔍 Qué Visualiza:

- **Gráfico de Barras:** Ingresos Totales por Tienda
- **Gráfico de Barras:** Calificación Promedio por Tienda
- **Gráfico Circular:** Distribución porcentual de ingresos entre tiendas

### ▶️ Cómo Ejecutarlo

1. Coloca el script y los `.csv` en el mismo directorio  
2. Asegúrate de tener `matplotlib` instalado  
3. Ejecuta:

```bash
python visualizacion_datos.py
```

---

## 📄 Recomendación (`recomendacion.md`)

Archivo complementario que incluye:

- **Análisis Realizado** (ingresos y calificaciones)
- **Recomendación:** Vender la **Tienda 4**
- **Justificación basada en datos**
- **Implicaciones para el Sr. João**
- **Limitaciones** (no se analizan costos operativos, entre otros)
- **Conclusión** que reafirma la decisión

---

## 📂 Estructura de Datos

Los datos por tienda incluyen:

- Producto, categoría y precios
- Costos de envío
- Fecha y lugar de compra
- Evaluaciones y métodos de pago
- Coordenadas geográficas de transacciones

---

Este conjunto de herramientas proporciona un marco sólido para analizar los datos de Alura Store y tomar decisiones informadas.  
Los análisis son **claros, modulares y fáciles de mantener o adaptar** a futuros escenarios comerciales.

## 📄 Licencia

Estos proyectos se distribuye bajo la licencia MIT. Puedes modificarlo y reutilizarlo libremente.

## 🧑‍💻 Autor

Oscar Daniel Cáceres

## ✅ Conclusión Final
