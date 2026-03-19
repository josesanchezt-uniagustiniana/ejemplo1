# FastAPI MVC - Guía de Configuración y Pruebas
## Uniagustiniana

Este proyecto implementa una API con FastAPI siguiendo el patrón Modelo-Vista-Controlador (MVC), utilizando SQLAlchemy para la persistencia en base de datos y Pytest para la validación de calidad.

🛠️ 1. Requisitos Previos
Python 3.10 o superior 🐍

Git (para el control de versiones)

💻 2. Instalación en Windows
Sigue estos pasos para preparar tu entorno de desarrollo local:

Clonar el repositorio:

```Bash
git clone <url-de-tu-repositorio>
cd ejemplo1
```

Crear el entorno virtual (.venv):

```Bash
python -m venv venv
```

Activar el entorno virtual:

En PowerShell:

```PowerShell
.\venv\Scripts\Activate.ps1
```
En CMD:
```DOS
.\venv\Scripts\activate.bat
```

Instalar dependencias:

```Bash
pip install -r requirements.txt
```
🧪 3. Ejecución de Pruebas Unitarias
Las pruebas están diseñadas para ejecutarse de forma aislada utilizando una base de datos SQLite en memoria.

Ejecución estándar:

```ash
python -m pytest -v
```
Ejecución con detalles de depuración (ver prints):

```Bash
python -m pytest -s
```

📊 4. Cobertura de Código (Coverage)
Para medir qué porcentaje de la lógica de la aplicación está siendo validada por los tests:

Generar reporte en consola:
```Bash
python -m pytest --cov=app --cov-report=term-missing
```

Generar reporte para SonarQube (XML):

```Bash
python -m pytest --cov=app --cov-report=xml
```
Esto creará un archivo coverage.xml en la raíz, el cual es detectado automáticamente por el pipeline de SonarQube. 📡

# Ejecución

Sobre la carpeta raíz del proyecto se podrá ejecutar el proyecto de la siguiente manera:

``` python
python -m uvicorn app.main:app --reload
```
Donde 
app.main: Se refiere al archivo main.py dentro de la carpeta app.

:app: Es el nombre de la variable donde instanciaste FastAPI().

--reload: Permite que el servidor se reinicie automáticamente cada vez que guardes un cambio.