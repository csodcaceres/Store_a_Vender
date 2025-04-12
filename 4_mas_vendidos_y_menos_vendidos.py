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
# ----- 2. Productos más y menos vendidos
#-------------------------------------------------------------------------------------------
def top_bottom_selling_products(df, n=5):
    """Identifica los n productos más y menos vendidos por cantidad."""
    product_counts = df['Producto'].value_counts()
    if n > 0:
        return product_counts.nlargest(n)
    elif n < 0:
        return product_counts.nsmallest(abs(n))
    else:
        return pd.Series()  # Devuelve una Serie vacía si n es 0

top_productos_tienda1 = top_bottom_selling_products(tienda1_df)
bottom_productos_tienda1 = top_bottom_selling_products(tienda1_df, n=-5)
top_productos_tienda2 = top_bottom_selling_products(tienda2_df)
bottom_productos_tienda2 = top_bottom_selling_products(tienda2_df, n=-5)
top_productos_tienda3 = top_bottom_selling_products(tienda3_df)
bottom_productos_tienda3 = top_bottom_selling_products(tienda3_df, n=-5)
top_productos_tienda4 = top_bottom_selling_products(tienda4_df)
bottom_productos_tienda4 = top_bottom_selling_products(tienda4_df, n=-5)

#-------------------------------------------------------------------------------------------
# --- 3. Imprimir los resultados en consola
#-------------------------------------------------------------------------------------------
def print_top_bottom_products(top_products, bottom_products, store_name):
    """Imprime los productos más y menos vendidos en la consola."""
    print(f"\n--- {store_name} ---")
    if not top_products.empty:
        print("\nProductos Más Vendidos (Cantidad):")
        print(top_products)
    else:
        print("\nNo hay productos más vendidos.")

    if not bottom_products.empty:
        print("\nProductos Menos Vendidos (Cantidad):")
        print(bottom_products)
    else:
        print("\nNo hay productos menos vendidos.")

print_top_bottom_products(top_productos_tienda1, bottom_productos_tienda1, 'Tienda 1')
print_top_bottom_products(top_productos_tienda2, bottom_productos_tienda2, 'Tienda 2')
print_top_bottom_products(top_productos_tienda3, bottom_productos_tienda3, 'Tienda 3')
print_top_bottom_products(top_productos_tienda4, bottom_productos_tienda4, 'Tienda 4')

