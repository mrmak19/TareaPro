# Tarea 2 de programación: Python con Bases de Datos

## 📖 Descripción
En este repositorio, contiene los ficheros requeridos para el correcto funcionamiento de la tarea 2. Se ha decidido por una temática clásica de un supermercado como objetivo de la base de datos. Se tratará de gestionar dicha base de datos a través de SQL Server.

## 🛠️ Requisitos previos
Se requiere de Microsoft SQL Server, ya que se hace uso de dicho servidor; se puede instalar en la web de [Microsoft SQL Server](https://www.microsoft.com/es-es/sql-server/sql-server-downloads).

Además de ello, se requiere de la librería *pyodbc* para que funcione el código correctamente. Esto se puede instalar mediante el siguiente comando:
```bash
pip install pyodbc
```

## Base de Datos
La base de datos del supermercado se organiza en cuatro tablas principales: Clientes, Productos, Pedidos y Detalles de Pedido. A continuación se detalla cada tabla y sus campos:

### Tabla Clientes

| Campo      | Tipo de dato      | Obligatorio | Clave     |
|------------|-----------------|------------|--------------|
| id_cliente | INT              | Sí         | PK          |
| nombre     | NVARCHAR(100)    | Sí         | -           |
| apellido   | NVARCHAR(100)    | Sí         | -           |
| email      | NVARCHAR(100)    | Sí         | Único       |
| telefono   | NVARCHAR(20)     | No         | -           |
| direccion  | NVARCHAR(255)    | No         | -           |

### Tabla Productos

| Campo       | Tipo de dato   | Obligatorio | Clave |
|-------------|----------------|------------|--------|
| id_producto | INT            | Sí         | PK     |
| nombre      | NVARCHAR(100)  | Sí         | -      |
| categoria   | NVARCHAR(50)   | No         | -      |
| precio      | DECIMAL(10,2)  | Sí         | -      |
| stock       | INT            | Sí         | -      |

### Tabla Pedidos

| Campo       | Tipo de dato   | Obligatorio | Clave        |
|-------------|----------------|-------------|-------------|
| id_pedido   | INT            | Sí          | PK          |
| id_cliente  | INT            | Sí          | FK → Clientes(id_cliente) |
| fecha       | DATETIME       | No (por defecto GETDATE()) | - |
| estado      | NVARCHAR(30)   | No (por defecto 'pagado') | - |

### Tabla Detalles de Pedido

| Campo         | Tipo de dato    | Obligatorio | Clave                          |
|----------------|----------------|-------------|--------------------------------|
| id_detalle     | INT            | Sí          | PK                             |
| id_pedido      | INT            | Sí          | FK → Pedidos(id_pedido)        |
| id_producto    | INT            | Sí          | FK → Productos(id_producto)    |
| cantidad       | INT            | Sí          | -                              |
| precio_unitario| DECIMAL(10,2)  | Sí          | -                              |

## 📁 Estructura del Proyecto
```bash
TareaPro/
├── Tarea2.py                       # Ejecutable y punto de partida
├── RellenarDatos.py                # Script que se encarga de poblar la base de datos
├── moduloSQL.py                    # Módulo propio con conexión a la base de datos
├── Modificaciones.py               # Script donde se albergan las querys solicitadas
├── Datos.py                        # Módulo propio donde albergan funciones para poblar con datos
├── DataExport.py                   # Script donde se exporta a CSV el resultado de una query
├── Analisis.ipynb                  # Notebook donde alberga el análisis de los resultados de la query
├── data/                            # Carpeta con los CSVs
│   └── clientes.csv                # CSV donde alberga los datos de los clientes
│   └── detalles_pedido.csv         # CSV donde alberga los detalles de cada pedido
│   └── pedidos.csv                 # CSV donde alberga los pedidos
│   └── productos.csv               # CSV donde alberga los datos de los productos
│   └── total_vendido.csv           # CSV resultante de la exportación de datos de la query
└── README.md                       # Este presente archivo
```

## 👨‍💻 Autor(es)
El proyecto ha sido desarrollado en contunto por **Yanjun Chen**, **Hengyi Du** y **Xiuhuang Zhan Zhang**.
Desarrollado como proyecto educativo para un trabajo de la universidad y para demostrar habilidades en:

- Manejo de SQL
- Manipulación de Base de Datos
- Tratamiento de base de datos en Python
- Creatividad