# Proyecto Nexos: Carga de Datos y Consulta de Inventario

Este proyecto ofrece una solución efectiva para simplificar y automatizar el proceso de cargar datos desde archivos CSV a una base de datos PostgreSQL dockerizada. El objetivo central es proporcionar una solución eficiente para importar, almacenar y consultar información estructurada desde archivos CSV, aprovechando una base de datos sólida y escalable.

## Características Destacadas

- Automatiza la carga de datos desde archivos CSV a una base de datos PostgreSQL.
- Ofrece una visualización interactiva de los datos cargados en forma de tabla.
- Proporciona acceso rápido y sencillo a la documentación de la API a través de Swagger.
- Configuración de la base de datos PostgreSQL mediante Docker para simplificar el entorno.

## Requisitos

- Django 4.2.4
- Python 3.10.0

## Configuración Rápida

1. **Clonar el Repositorio**:
   ```bash
   git clone <URL del repositorio>
   ```

2. **Crear un Entorno Virtual**:
   ```bash
   python -m venv venv
   ```

3. **Activar el Entorno Virtual**:
   ```bash
   source venv/bin/activate
   ```

4. **Instalar las Dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realizar las Migraciones**:
   ```bash
   python manage.py migrate
   ```

6. **Iniciar el Servidor**:
   ```bash
   python manage.py runserver
   ```

Una vez que el servidor esté en funcionamiento, se abrirá automáticamente una pestaña en tu navegador con la dirección http://127.0.0.1:8000/. En esta página, encontrarás una tabla que muestra el listado de inventarios cargados en la base de datos. Además, hay un botón que te llevará a la documentación interactiva de la API mediante Swagger.