import pyodbc

def connexionSQL(host: str,db: str, usr:str, passwd: str):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={host};"
        f"DATABASE={db};"
        f"UID={usr};"
        f"PWD={passwd};"
        "TrustServerCertificate=yes;",
        autocommit=True
    )
    return conn
    