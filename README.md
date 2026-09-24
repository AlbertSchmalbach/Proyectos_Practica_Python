# Proyectos de practica en Python

Coleccion de proyectos pequenos para practicar Python, interfaces graficas, manejo de datos y persistencia de informacion.

## Proyectos

### `ListaTarea`

Aplicacion grafica de lista de tareas desarrollada con **PyQt6**. Permite:

- Agregar tareas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardar y cargar las tareas desde `tareas.txt`.

### `Empleados`

Aplicacion grafica para registrar empleados con **PyQt5**. Permite introducir nombre, apellido, profesion y sueldo, calcular el sueldo neto y exportar los datos a un archivo Excel.

Tecnologias utilizadas:

- PyQt5
- pandas
- openpyxl

## Requisitos

- Python 3.10 o una version posterior.
- Las dependencias indicadas en cada proyecto.

Cada proyecto tiene su propio entorno virtual para mantener sus dependencias separadas.

## Ejecucion

### Lista de tareas

En PowerShell:

```powershell
cd ListaTarea
.\env\Scripts\Activate.ps1
python lista_tarea.py
```

Si el sistema bloquea la activacion de scripts, tambien se puede ejecutar directamente:

```powershell
cd ListaTarea
.\env\Scripts\python.exe lista_tarea.py
```

Las tareas se guardan en `ListaTarea/tareas.txt`.

### Registro de empleados

En PowerShell:

```powershell
cd Empleados
.\env\Scripts\Activate.ps1
python empleado_form.py
```

O directamente con el interprete del entorno:

```powershell
cd Empleados
.\env\Scripts\python.exe empleado_form.py
```

El boton **Exportar Excel** genera `Empleados/data_empleado.xlsx`.

## Instalar dependencias

Si es necesario reconstruir un entorno virtual, se pueden instalar las dependencias con:

```powershell
python -m pip install PyQt6
```

Para `Empleados`:

```powershell
python -m pip install PyQt5 pandas openpyxl
```

## Estructura

```text
Proyects_Python/
|-- Empleados/
|   |-- empleado_form.py
|   |-- data_empleado.xlsx
|   `-- env/
|-- ListaTarea/
|   |-- lista_tarea.py
|   |-- tareas.txt
|   |-- explicacion_lista_tarea.md
|   `-- env/
|-- .gitignore
`-- README.md
```

## Objetivo

Este repositorio sirve como espacio de aprendizaje. Los proyectos pueden evolucionar con nuevas practicas de Python, mejoras de interfaz, validaciones, persistencia y organizacion del codigo.
