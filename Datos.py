import pyodbc
import pandas as pd

def insertar_clientes(csv_path, conn):

    # Leer CSV
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()

    # Recorrer filas e insertar
    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO clientes (nombre, apellido, email, telefono, direccion)
                VALUES (?, ?, ?, ?, ?)
            """, 
            row["nombre"], 
            row["apellido"], 
            row["email"], 
            row["telefono"], 
            row["direccion"]
            )
        except pyodbc.Error as e:
            print(f" Error en fila {row.to_dict()}: {e}")
            continue  

    print("Inserción completada.")


def insertar_productos(csv_path, conn):
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO productos (nombre, categoria, precio, stock)
                VALUES (?, ?, ?, ?)
            """,
            row["nombre"],
            row["categoria"],
            row["precio"],
            row["stock"]
        )
        except pyodbc.Error as e:
            print(f"Error insertando producto {row.to_dict()}: {e}")
            continue
        
    print("Productos insertados correctamente.")
    
def insertar_pedidos(csv_path, conn):
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO pedidos (id_cliente, fecha, estado)
                VALUES (?, ?, ?)
            """,
            row["id_cliente"],
            row["fecha"],
            row["estado"]
        )
        except pyodbc.Error as e:
            print(f"Error insertando pedido {row.to_dict()}: {e}")
            continue

    print("Pedidos insertados correctamente.")

def insertar_detalles(csv_path, conn):
    df = pd.read_csv(csv_path)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario)
                VALUES (?, ?, ?, ?)
            """,
            row["id_pedido"],
            row["id_producto"],
            row["cantidad"],
            row["precio_unitario"]
        )
        except pyodbc.Error as e:
            print(f"Error insertando detalle {row.to_dict()}: {e}")
            continue

    print("Detalles insertados correctamente.")