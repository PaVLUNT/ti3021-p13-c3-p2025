import oracledb
import os
from datetime import datetime

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

# Conexión Reutilizable
def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)

# Crear Tabla

def create_schema(): -> None
    pass

def create_table() -> None:

    ddl = (
        "CREATE TABLE personas ("
        "id INTEGER PRIMARY KEY,"
        "rut NUMBER (8),"
        "nombres VARCHAR2(64),"
        "apellidos VARCHAR2(64),"
        "fecha_nacimiento DATE,"
        ")"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(ddl)
                print("Tabla 'personas' creada.")
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err}")

# Insertar Datos
def create_persona(rut, nombres, apellidos, fecha_nacimiento, cod_area, numero_telefono):
    sql = (
        "INSERT INTO personas (rut, nombres, apellidos, fecha_nacimiento, cod_area, numero_telefono)"
        "VALUES (:rut, :nombres, :apellidos, :fecha_nacimiento, :cod_area, :numero_telefono)"
    )
    bind_fecha = None
    if fecha_nacimiento: bind_fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {
                "rut": rut,
                "nombres": nombres,
                "apellidos": apellidos,
                "fecha_nacimiento": bind_fecha,
                "cod_area": cod_area,
                "numero_telefono": numero_telefono,
            })
            conn.commit()
            print(f"Persona con RUT={rut} creada.")


