import logging
import os
import sqlite3
from pathlib import Path

import pandas as pd
import pyodbc
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SQL_SERVER", "").strip()
PORT = os.getenv("SQL_PORT", "").strip()
DATABASE = os.getenv("SQL_DATABASE", "").strip()
USER = os.getenv("SQL_USER", "").strip()
PWD = os.getenv("SQL_PASSWORD", "").strip()

ODBC_DRIVER = os.getenv(
    "ODBC_DRIVER",
    "SQL Server Native Client 11.0"
).strip()

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_SQLITE_DB = BASE_DIR / "reporteops.db"


def construir_cadena_conexion():
    """
    Usa SQLite local cuando exista la base reporteops.db.
    Si no existe, conserva el comportamiento anterior con SQL Server.
    """

    sqlite_path = os.getenv(
        "REPORTEOPS_DB",
        str(DEFAULT_SQLITE_DB)
    ).strip()

    if os.path.exists(sqlite_path):
        return sqlite_path

    if not SERVER or not DATABASE:
        raise RuntimeError(
            "Faltan variables de entorno o no existe la base SQLite local"
        )

    server = f"{SERVER},{PORT}" if PORT else SERVER

    if USER and PWD:
        auth = f"UID={USER};PWD={PWD};"
    else:
        auth = "Trusted_Connection=yes;"

    return (
        f"DRIVER={{{ODBC_DRIVER}}};"
        f"SERVER={server};"
        f"DATABASE={DATABASE};"
        f"{auth}"
    )


def obtener_conexion():

    conn_str = construir_cadena_conexion()

    if os.path.exists(conn_str) and not conn_str.lower().startswith("driver="):
        logging.info("Conectando a SQLite...")
        return sqlite3.connect(conn_str)

    logging.info("Conectando a SQL Server...")
    return pyodbc.connect(conn_str)


def leer_query(nombre_archivo="query.txt"):

    ruta_query = Path(nombre_archivo)

    if not ruta_query.exists():
        raise FileNotFoundError(
            f"No existe el archivo: {nombre_archivo}"
        )

    with open(
        ruta_query,
        "r",
        encoding="utf-8"
    ) as archivo:

        return archivo.read()


def ejecutar_consulta(
    op,
    archivo_query="query.txt"
):

    query_template = leer_query(
        archivo_query
    )

    query = query_template.format(
        op=op
    )

    logging.info(
        f"Ejecutando consulta para OP {op} usando {archivo_query}"
    )

    with obtener_conexion() as conn:

        df = pd.read_sql(
            query,
            conn
        )

    return df