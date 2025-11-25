import moduloSQL as sql
# variables para conectar a sql
host="localhost"
DB_NAME = "TareaPro"
usr="sa"
passwd="asdf1234"

conn = sql.connexionSQL(host=host,db="master",usr=usr,passwd=passwd)
cursor_master = conn.cursor()

cursor_master.execute("""
    SELECT name 
    FROM sys.databases 
    WHERE name = ?
""", DB_NAME)

exists = cursor_master.fetchone()

if not exists:
    print(f"La base de datos '{DB_NAME}' NO existe. Creándola...")
    cursor_master.execute(f"CREATE DATABASE {DB_NAME}")
    conn.commit()
    print("Base creada exitosamente.")
else:
    print(f"La base de datos '{DB_NAME}' ya existe.")
    
    
conn.close()

print(f"Conectando a la base de datos '{DB_NAME}'...")

conn_tarea = sql.connexionSQL(host=host,db=DB_NAME,usr=usr,passwd=passwd)

print("Conexión exitosa a TareaPro.")

cursor = conn_tarea.cursor()

sql_clientes = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='clientes' AND xtype='U')
BEGIN
    CREATE TABLE clientes (
        id_cliente INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL,
        apellido NVARCHAR(100) NOT NULL,
        email NVARCHAR(100) NOT NULL UNIQUE,
        telefono NVARCHAR(20) NOT NULL UNIQUE,
        direccion NVARCHAR(255) NOT NULL
    );
END
"""
sql_productos = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='productos' AND xtype='U')
BEGIN
    CREATE TABLE productos (
        id_producto INT IDENTITY(1,1) PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL,
        categoria NVARCHAR(50),
        precio DECIMAL(10,2) NOT NULL,
        stock INT NOT NULL
    );
END
"""

sql_pedidos = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='pedidos' AND xtype='U')
BEGIN
    CREATE TABLE pedidos (
        id_pedido INT IDENTITY(1,1) PRIMARY KEY,
        id_cliente INT NOT NULL,
        fecha DATETIME DEFAULT GETDATE(),
        estado NVARCHAR(30) DEFAULT 'pagado',
        CONSTRAINT fk_pedidos_cliente FOREIGN KEY (id_cliente)
            REFERENCES clientes(id_cliente)
            ON DELETE CASCADE
    );
END
"""

sql_detalles = """
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='detalles_pedido' AND xtype='U')
BEGIN
    CREATE TABLE detalles_pedido (
        id_detalle INT IDENTITY(1,1) PRIMARY KEY,
        id_pedido INT NOT NULL,
        id_producto INT NOT NULL,
        cantidad INT NOT NULL,
        precio_unitario DECIMAL(10,2) NOT NULL,
        CONSTRAINT fk_detalle_pedido FOREIGN KEY (id_pedido)
            REFERENCES pedidos(id_pedido)
            ON DELETE CASCADE,
        CONSTRAINT fk_detalle_producto FOREIGN KEY (id_producto)
            REFERENCES productos(id_producto)
            ON DELETE CASCADE
    );
END
"""

# Ejecutar todas las sentencias
cursor.execute(sql_clientes)
cursor.execute(sql_productos)
cursor.execute(sql_pedidos)
cursor.execute(sql_detalles)

conn_tarea.commit()
conn_tarea.close()

print("Tablas creadas/verificadas correctamente.")
