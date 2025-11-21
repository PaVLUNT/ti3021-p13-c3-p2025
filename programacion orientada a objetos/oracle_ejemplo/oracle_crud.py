import oracledb
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Tabla creada. \n {query}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo crear la tabla: {err} \n {query}")

tables = [
        (
            "CREATE TABLE PERROS ("
            "id_perro INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad NUMBER(10),"
            "historial_vacunas DATE"
            ")"
        ),
        (
            "CREATE TABLE GATOS ("
            "id_gato INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad VARCHAR(10),"
            "esterilizado VARCHAR(1)"
            ")"
        ),
        (
            "CREATE TABLE AVES ("
            "id_ave INTEGER PRIMARY KEY,"
            "nombre VARCHAR(60),"
            "edad NUMBER(10),"
            "control_vuelo VARCHAR(50),"
            "tipo_jaula VARCHAR(50)"
            ")"
        ),
        (
            "CREATE TABLE HISTORIAL_MEDICO ("
            "id_historial INTEGER PRIMARY KEY,"
            "observaciones VARCHAR(100),"
            "tratamientos VARCHAR(200)"
            ")"
        )
]

for query in tables:
    create_schema(query)            

# Create - Crear tablas

def create_perro(
        id_perro:int,
        nombre:str,
        edad:int,
        historial_vacunas:datetime
):
    sql = (        
        "INSERT INTO PERROS (id_perro, nombre, edad, historial_vacunas)"
        "VALUES (:id_perro, :nombre, :edad, :historial_vacunas)"
    )
    parametros = {
        "id_perro": id_perro,
        "nombre": nombre,
        "edad": edad,
        "historial_vacunas": historial_vacunas
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")
        
        
def create_gato(
        id_gato:int,
        nombre:str,
        edad:int,
        esterilizado:str
):
    sql = (        
        "INSERT INTO GATOS (id_gato, nombre, edad, historial_vacunas)"
        "VALUES (:id_gato, :nombre, :edad, :historial_vacunas)"
    )
    parametros = {
        "id_gato": id_gato,
        "nombre": nombre,
        "edad": edad,
        "esterilizado": esterilizado
    }
    
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def create_ave(
        id_ave:int,
        nombre:str,
        edad:int,
        control_vuelo:str,
        tipo_jaula:str
):
    sql = (
        "INSERT INTO AVES (id_ave, nombre, edad, control_vuelo, tipo_jaula)"
        "VALUES (:id_ave, :nombre, :edad, :control_vuelo, :tipo_jaula)"
    )
    parametros = {
        "id_ave": id_ave,
        "nombre": nombre,
        "edad": edad,
        "control_vuelo": control_vuelo,
        "tipo_jaula": tipo_jaula
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")


def create_HMedico(
        id_historial:int,
        observaciones:str,
        tratamientos:str
):
    sql = (
        "INSERT INTO HISTORIAL_MEDICO (id_historial, observaciones, tratamientos)"
        "VALUES (:id_historial, :observaciones, :tratamientos)"
    )
    parametros = {
        "id_historial": id_historial,
        "observaciones": observaciones,
        "tratamientos": tratamientos       
    }

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
                print(f"Dato insertado. \n {parametros}")
            conn.commit()
    except oracledb.DatabaseError as e:
        err = e
        print(f"No se pudo insertar el dato: {err} \n {parametros}")

# Read - Consulta de datos

def read_aves():
    sql = (
        "SELECT * FROM AVES"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla 'AVES'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_aves_by_id():
    sql = (
        "SELECT * FROM AVES WHERE id_ave = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla 'AVES' por 'ID_AVE'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_gatos():
    sql = (
        "SELECT * FROM GATOS"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla 'GATOS'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_gatos_by_id():
    sql = (
        "SELECT * FROM GATOS WHERE id_gato = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla 'GATOS' por 'ID_GATO'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_historial_medico():
    sql = (
        "SELECT * FROM HISTORIAL_MEDICO"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla 'HISTORIAL_MEDICO'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_historial_medico_by_id():
    sql = (
        "SELECT * FROM HISTORIAL_MEDICO WHERE id_historial = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla 'HISTORIAL_MEDICO' por 'ID_HISTORIAL'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_perros():
    sql = (
        "SELECT * FROM PERROS"
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql)
                print(f"Consulta a la tabla 'PERROS'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def read_perros_by_id():
    sql = (
        "SELECT * FROM PERROS WHERE id_perro = :id"
    )

    parametros = {"id": id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                resultados = cur.execute(sql,parametros)
                print(f"Consulta a la tabla 'AVES' por 'ID_AVE'")
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

from typing import Optional

# Update - Actualizar datos

def update_perros(id, nombre: Optional[str] = None, edad: Optional[str] = None, historial_vacunas: Optional[str] = None):
    modificaciones = []
    binds  = {"id_perro": id}

    if id is not None:
        modificaciones.append("id_perro =: id")
        binds["id_perro"] = id
    
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        binds["nombre"] = nombre
    
    if edad is not None:
        modificaciones.append("edad =: edad")
        binds["edad"] = edad
    
    if historial_vacunas is not None:
        modificaciones.append("historial_vacunas =: historial_vacunas")
        binds["historial_vacunas"] = datetime.strptime(historial_vacunas, "%Y-%m-%d")
    
    if not modificaciones:
        print("No hay campo para actualizar.")
        return
    
    sql = f"UPDATE PERROS SET {",".join(modificaciones)} WHERE id_perro =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, binds)
        conn.commit()
        print(f"Perro con ID={id} actualizado.")

def update_gatos(id, nombre: Optional[str] = None, edad: Optional[str] = None, esterilizado: Optional[str] = None):
    modificaciones = []
    binds  = {"id_gatp": id}

    if id is not None:
        modificaciones.append("id_gato =: id")
        binds["id_gato"] = id
    
    if nombre is not None:
        modificaciones.append("nombre =: nombre")
        binds["nombre"] = nombre
    
    if edad is not None:
        modificaciones.append("edad =: edad")
        binds["edad"] = edad
    
    if esterilizado is not None:
        modificaciones.append("esterilizado =: esterilizado")
        binds["esterilizado"] = esterilizado
    
    if not modificaciones:
        print("No hay campo para actualizar.")
        return
    
    sql = f"UPDATE GATOS SET {",".join(modificaciones)} WHERE id_gato =: id"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, binds)
        conn.commit()
        print(f"Gato con ID={id} actualizado.")

# Delete - Eliminacion de datos

def delete_perros(id: int):
    sql = (
        "DELETE FROM PERROS WHERE id_perro = :id"
    )

    parametros  = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def delete_gatos(id: int):
    sql = (
        "DELETE FROM GATOS WHERE id_gato = :id"
    )

    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def delete_aves(id: int):
    sql = (
        "DELETE FROM AVES WHERE id_ave = :id"
    )

    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def delete_historial_medico(id: int):
    sql = (
        "DELETE FROM HISTORIAL_MEDICO WHERE id_historial = :id"
    )

    parametros = {"id" : id}

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql,parametros)
            conn.commit()
            print(f"Dato eliminado \n {parametros}")
    except oracledb.DatabaseError as e:
        err = e
        print(f"Error al insertar datos: {err}")

def main():
    while True:
        print(
            """
            ===========================================
            |         ☺ CRUD CON ORACLESQL ☺          |
            ===========================================
            | 1. APLICAR ESQUEMA EN LA BASE DE DATOS  |
            | 2. TABLA PERROS                         |
            | 3. TABLA GATOS                          |
            | 4. TABLA AVES                           |
            | 5. TABLA HISTORIAL MEDICO               |
            | 0. SALIR                                |
            ===========================================
            """
        )
        opcion = input("Selecciona una opcion [1-5, 0 para salir]: ")

        if opcion == "0":
            os.system("cls")
            print("Volviendo al menú principal. o((>ω< ))o")
            input("Presiona ENTER para continuar...")
            break
        elif opcion == "1":
            try:
                id = int(input("Ingrese el id numerico del perro: "))
                nombre = input("Ingresa el nombre del perro: ")
                edad = int(input("Ingresa la edad del perro: "))
                historial_vacunas = input("Ingresa el historial de vacunas: ")

                create_perro(id, nombre, edad, historial_vacunas)
                input("Presiona ENTER para continuar...")
            except ValueError:
                return print("Ingresaste un valor no numerico.")
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        else:
            print("Opcion Invalida.")
            input("Presiona ENTER para continuar...")
            break

if __name__ == "__main__":
    main()