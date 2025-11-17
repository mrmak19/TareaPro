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

print("Comprobacion de si existe la tabla productos")
tabla_producto="Porducto"
cursor = conn_tarea.cursor()
cursor.execute(f"""
    SELECT * 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_NAME = '{tabla_producto}'
""")

table_exists = cursor.fetchone()