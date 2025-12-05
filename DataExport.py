import pandas as pd
import moduloSQL as sql
import matplotlib as plt

host="localhost"
DB_NAME = "TareaPro"
usr="sa"
passwd="asdf1234"

conn_tarea = sql.connexionSQL(host=host,db=DB_NAME,usr=usr,passwd=passwd)
cursor = conn_tarea.cursor()
print("Conexión exitosa a TareaPro.")

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
cursor.execute(query5)

# Obtener nombres de columnas
columns = [col[0] for col in cursor.description]

# Obtener datos
rows = cursor.fetchall()

# Crear DataFrame SIN WARNING
df = pd.DataFrame.from_records(rows, columns=columns)

# Guardar CSV
df.to_csv("total_vendido.csv", index=False)
# Cerramos conexión
conn_tarea.commit()
conn_tarea.close()