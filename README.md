# Comparativa Órdenes de Producción

## Real vs. Previsto

Aplicación web desarrollada con **Python y Streamlit** para comparar cantidades previstas y reales en órdenes de producción, detectar desvíos y facilitar el control de costos.

<p align="left">
  <a href="https://costos-reporteops.streamlit.app/">
    <img src="https://img.shields.io/badge/Demo-Online-28A745?logo=googlechrome&logoColor=white&style=for-the-badge" height="40">
  </a>
  <a href="https://www.linkedin.com/in/claudiogabrielalonso/">
    <img src="https://img.shields.io/badge/LinkedIn-Perfil-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" height="40">
  </a>
</p>

## Sobre el proyecto

**Reporte OPs** permite analizar órdenes de producción cerradas, comparando cantidades **previstas vs. reales** para detectar desvíos y facilitar el control de costos.


## Objetivo

Facilitar el análisis de:

-   Cantidades previstas y reales.
-   Órdenes de producción e insumos.
-   Desvíos y costos asociados.


## Resultado

Automatiza el procesamiento y consolidación de datos para su análisis.

-   Comparación Real vs. Previsto.
-   Detección de desvíos.
-   Filtrado de resultados.
-   Exportación a Excel.


## Funcionalidades

-   Rango de fechas.
-   Consulta de OPs cerradas.
-   Filtro de diferencias.
-   Consolidación por OP e insumo.
-   Exportación a Excel.


## Módulos

Módulo

Descripción

`app.py`

Interfaz Streamlit y flujo principal

`db.py`

Conexión y extracción de datos

`transformacion.py`

Procesamiento y transformación de datos

`query.txt`

Consulta SQL principal

`querygramaje.txt`

Consulta SQL complementaria

`requirements.txt`

Dependencias del proyecto


## Arquitectura

```
Usuario
   ↓
Streamlit
   ↓
Extracción SQL
   ↓
DataFrame
   ↓
Normalización y transformación
   ↓
Comparación Real / Previsto
   ↓
Filtros y consolidación
   ↓
Resultado / Excel
```


## Datos y procesamiento

La aplicación puede trabajar con **SQL Server** como fuente principal y **SQLite** para entornos locales.

La extracción se realiza mediante consultas SQL parametrizadas por rango de fechas.

Posteriormente, los datos son procesados mediante `Pandas` para:

-   Normalizar y estandarizar datos.
-   Crear columnas derivadas.
-   Separar previstos y reales.
-   Consolidar y agrupar registros.
-   Preparar el dataset final para análisis.


## Tecnologías

### Lenguaje

`Python`

### Framework

`Streamlit`

### Datos

`Pandas` · `NumPy`

### Bases de datos

`SQL Server` · `SQLite`

### Herramientas

`pyodbc` · `openpyxl` · `python-dotenv`

----------

## Instalación y ejecución

```
git clone URL_REPOSITORIO
cd ReporteOPs

python -m venv venv
```

Activar el entorno virtual:

```
# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

Instalar dependencias:

```
pip install -r requirements.txt
```

Configurar las variables de conexión a la base de datos en `.env` y ejecutar:

```
streamlit run app.py
```
La aplicación estará disponible en:
```
http://localhost:8501
```

----------

## Configuración

La conexión a la base de datos utiliza variables de entorno:

```
SQL_SERVER=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
```
