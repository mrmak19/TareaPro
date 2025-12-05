import moduloSQL as sql
import pandas as pd
# variables para conectar a sql
host="localhost"
DB_NAME = "TareaPro"
usr="sa"
passwd="asdf1234"
conn = sql.connexionSQL(host=host,db=DB_NAME,usr=usr,passwd=passwd)
cursor = conn.cursor()

cursor.execute("""
        INSERT INTO clientes (nombre, apellido, email, telefono, direccion)
        VALUES 
        ('Juan', 'Pérez', 'juan.perez@email.com', '3586477', 'Calle 123'),
        ('Ana', 'Gómez', 'ana.gomez@email.com', '555-5678', 'Avenida 456'),
        ('Luis', 'Martínez', 'luis.martinez@email.com', '555-9012', 'Calle 789'),
        ('Hengyi', 'Du', 'hengyi.du@email.com', '1001964524', 'Calle hernani 34'),
        ('Mario', 'Martínez', 'mario.martinez@email.com', '555-9013', 'Calle 789')
    """)
print("Clientes insertados")

cursor.execute("""
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES
        ('Laptop', 'Electrónica', 1200.50, 10),
        ('Camiseta', 'Ropa', 20.00, 50),
        ('Silla', 'Hogar', 150.75, 15),
        ('mesa', 'Hogar', 230.75, 10),
        ('balon', 'Juguetes', 9.75, 105)
    """)
print("Productos insertados")

cursor.execute("""
        INSERT INTO pedidos (id_cliente, fecha, estado)
        VALUES
        (1, GETDATE(), 'pagado'),
        (2, GETDATE(), 'entregado'),
        (3, GETDATE(), 'a recoger'),
        (4, GETDATE(), 'cancelado'),
        (5, GETDATE(), 'pagado')
    """)
print("Pedidos insertados")

cursor.execute("""
        INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario)
        VALUES
        (1, 1, 1, 1200.50),
        (2, 2, 3, 20.00),
        (3, 3, 2, 150.75),
        (4, 3, 4, 78.95),
        (5, 3, 2, 200.75)
    """)
print("Detalles insertados")

cursor.execute("UPDATE clientes SET telefono='555-9999' WHERE id_cliente=1")
cursor.execute("UPDATE clientes SET telefono='555-8888' WHERE id_cliente=20")
print("Teléfonos modificados")

cursor.execute("UPDATE clientes SET direccion='Nueva Calle 101' WHERE id_cliente=14")
cursor.execute("UPDATE clientes SET direccion='Avenida Renovada 202' WHERE id_cliente=13")
print("Direcciones modificadas")


cursor.execute("UPDATE pedidos SET estado='entregado' WHERE id_pedido=12")
cursor.execute("UPDATE pedidos SET estado='cancelado' WHERE id_pedido=15")
print("Estados de pedidos modificados")

print("Actualización completa")

# Consultas

# 1 Clientes con pedidos cancelados.
query1 = """
SELECT p.id_pedido, c.nombre, c.apellido, p.fecha, p.estado
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
WHERE p.estado = 'cancelado';
"""
df1 = pd.read_sql(query1, conn)
print(df1, "\n")

# 2 el promedio de ingresos
query2 = "SELECT AVG(precio_unitario) AS precio_promedio FROM detalles_pedido;"
df2 = pd.read_sql(query2, conn)
print(df2, "\n")

# 3 Cliente con mas pedido
query3 = """
SELECT Top 3 c.id_cliente, c.nombre, c.apellido, COUNT(p.id_pedido) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente, c.nombre, c.apellido
ORDER BY total_pedidos DESC;
"""
df3 = pd.read_sql(query3, conn)
print(df3, "\n")

# 4 Producto mas vendido
query4 = """
SELECT Top 5 pr.id_producto, pr.nombre, SUM(dp.cantidad) AS total_vendido
FROM productos pr
JOIN detalles_pedido dp ON pr.id_producto = dp.id_producto
GROUP BY pr.id_producto, pr.nombre
ORDER BY total_vendido DESC;
"""
df4 = pd.read_sql(query4, conn)
print(df4, "\n")

# 5 Total vendido por producto y cantidad de pedidos realizados por cliente
query5 = """
SELECT 
    p.id_pedido,
    c.nombre,
    c.apellido,
    SUM(dp.cantidad * dp.precio_unitario) AS total_pedido,
    pedidos_cliente.numero_pedidos
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
JOIN detalles_pedido dp ON p.id_pedido = dp.id_pedido
JOIN (
    SELECT id_cliente, COUNT(*) AS numero_pedidos
    FROM pedidos
    GROUP BY id_cliente
) AS pedidos_cliente
ON c.id_cliente = pedidos_cliente.id_cliente
GROUP BY p.id_pedido, c.id_cliente, c.nombre, c.apellido, pedidos_cliente.numero_pedidos
ORDER BY total_pedido DESC;

"""
df5 = pd.read_sql(query5, conn)
print(df5, "\n")

# Eliminar registros

cursor.execute("DELETE FROM detalles_pedido WHERE id_detalle = 1")
print("\n detalle con id 1 eliminado")

cursor.execute("DELETE FROM pedidos WHERE id_pedido = 2")
print("\n pedido con id 2 eliminado")

cursor.execute("DELETE FROM productos WHERE id_producto = 3")
print("\n producto con id 3 eliminado")

cursor.execute("DELETE FROM clientes WHERE id_cliente = 25")
print("\n cliente con id 25 eliminado")

conn.commit()
conn.close()