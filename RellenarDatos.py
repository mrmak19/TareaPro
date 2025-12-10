import Datos as data
import moduloSQL as sql
# variables para conectar a sql
host="localhost"
DB_NAME = "TareaPro"
usr="sa"
passwd="asdf1234"

url_cliente = "data/clientes.csv"
url_productos = "data/productos.csv"
url_pedidos = "data/pedidos.csv"
url_detalles = "data/detalles_pedido.csv"

conn = sql.connexionSQL(host=host,db=DB_NAME,usr=usr,passwd=passwd)

data.insertar_clientes(csv_path=url_cliente,conn=conn)
data.insertar_productos(csv_path=url_productos,conn=conn)
data.insertar_pedidos(csv_path=url_pedidos,conn=conn)
data.insertar_detalles(csv_path=url_detalles,conn=conn)

conn.commit()
conn.close()