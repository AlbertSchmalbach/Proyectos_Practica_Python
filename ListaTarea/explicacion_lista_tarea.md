# Explicación del programa Lista de Tareas

## Objetivo general

El programa crea una aplicación gráfica de lista de tareas usando **PyQt6**. Permite:

- Cargar tareas guardadas en `tareas.txt`.
- Agregar nuevas tareas.
- Marcar tareas como completadas.
- Eliminar tareas.
- Guardar los cambios automáticamente.

El archivo `tareas.txt` utiliza el siguiente formato:

```text
nombre de la tarea|estado
```

El estado `0` significa que la tarea está pendiente y el estado `1` significa que está completada.

## Explicación línea por línea

### Importaciones

```python
import sys
```

Importa el módulo `sys`, utilizado al final para enviar los argumentos del sistema a PyQt y cerrar correctamente la aplicación.

```python
import os
```

Importa `os`, que permite comprobar si existe el archivo `tareas.txt`.

```python
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLineEdit, QMessageBox, QHBoxLayout, QListWidgetItem
)
```

Importa los componentes visuales de PyQt6:

- `QApplication`: controla la aplicación gráfica.
- `QWidget`: representa la ventana principal.
- `QVBoxLayout`: organiza elementos verticalmente.
- `QPushButton`: crea botones.
- `QListWidget`: muestra una lista de tareas.
- `QLineEdit`: permite escribir texto.
- `QMessageBox`: muestra mensajes y advertencias.
- `QHBoxLayout`: organiza elementos horizontalmente.
- `QListWidgetItem`: representa un elemento individual de la lista.

```python
from PyQt6.QtGui import QFont, QBrush, QColor
```

Importa clases para modificar el aspecto visual:

- `QFont`: representa el estilo de la letra.
- `QBrush`: permite definir el pincel utilizado para pintar texto.
- `QColor`: representa un color.

```python
archivo = "tareas.txt"
```

Guarda en una variable el nombre del archivo donde se almacenan las tareas.

## Función `cargar_tareas`

```python
def cargar_tareas():
```

Define una función encargada de cargar las tareas desde el archivo.

```python
    if os.path.exists(archivo):
```

Comprueba si existe el archivo `tareas.txt`. Si no existe, la aplicación comienza con una lista vacía.

```python
        with open(archivo, 'r', encoding="utf-8") as contenido_archivo:
```

Abre el archivo en modo lectura. El parámetro `encoding="utf-8"` permite trabajar correctamente con tildes y otros caracteres especiales. La instrucción `with` cierra el archivo automáticamente.

```python
            for linea in contenido_archivo:
```

Recorre el archivo línea por línea.

```python
                tarea, estado_tarea = linea.strip().split("|")
```

El método `strip()` elimina espacios y saltos de línea. Después, `split("|")` divide cada línea usando el carácter `|`.

Por ejemplo:

```text
Presentar Conferencia|0
```

se separa en:

```python
tarea = "Presentar Conferencia"
estado_tarea = "0"
```

```python
                elemento_lista = crear_elemento_lista_widget(tarea, estado_tarea == "1")
```

Crea el elemento visual de la tarea. La expresión `estado_tarea == "1"` devuelve `True` si la tarea está completada y `False` si está pendiente.

```python
                lista_tareas.addItem(elemento_lista)
```

Añade la tarea creada a la lista visual de la ventana.

## Función `crear_elemento_lista_widget`

```python
def crear_elemento_lista_widget(texto, completado=False):
```

Define una función que crea un elemento para la lista. Recibe el texto de la tarea y, opcionalmente, su estado. Por defecto, la tarea no está completada.

```python
    elemento_lista = QListWidgetItem(texto)
```

Crea un elemento de lista con el texto recibido.

```python
    fuente = QFont()
```

Crea un objeto que representa la fuente o estilo de letra.

```python
    fuente.setStrikeOut(completado)
```

Activa o desactiva el tachado del texto. Si `completado` es `True`, la tarea aparece tachada.

```python
    elemento_lista.setFont(fuente)
```

Aplica la fuente al elemento de la lista.

```python
    if completado:
```

Comprueba si la tarea está completada.

```python
        elemento_lista.setForeground(QBrush(QColor("gray")))
```

Cambia el color del texto a gris cuando la tarea está completada.

```python
    return elemento_lista
```

Devuelve el elemento creado para poder añadirlo a `lista_tareas`.

## Función `agregar_tarea`

```python
def agregar_tarea():
```

Define la función que se ejecuta al pulsar el botón **Agregar**.

```python
    texto = tareas_input_text.text().strip()
```

Obtiene el texto escrito por el usuario y elimina espacios innecesarios al principio y al final.

```python
    if texto:
```

Comprueba que el usuario haya escrito algo. Una cadena vacía se considera falsa.

```python
        elemento_lista = crear_elemento_lista_widget(texto)
```

Crea un nuevo elemento para la tarea. Como no se indica el estado, comienza como pendiente.

```python
        lista_tareas.addItem(elemento_lista)
```

Añade la nueva tarea a la lista visual.

```python
        tareas_input_text.clear()
```

Limpia el campo de texto para permitir escribir otra tarea.

```python
        guardar_tareas()
```

Guarda la lista actualizada en `tareas.txt`.

```python
    else:
```

Se ejecuta si el campo de texto estaba vacío.

```python
        QMessageBox.warning(ventana, "Advertencia", "Escribe una tarea...")
```

Muestra una ventana de advertencia indicando que se debe escribir una tarea.

## Función `guardar_tareas`

```python
def guardar_tareas():
```

Define la función que guarda todas las tareas en el archivo.

```python
    with open(archivo, "w", encoding="utf-8") as texto_archivo:
```

Abre el archivo en modo escritura. El modo `"w"` reemplaza el contenido anterior o crea el archivo si no existe.

```python
        for elemento_lista_indice in range(lista_tareas.count()):
```

Recorre las posiciones de todos los elementos de la lista.

```python
            elemento_lista = lista_tareas.item(elemento_lista_indice)
```

Obtiene la tarea que corresponde al índice actual.

```python
            texto = elemento_lista.text()
```

Obtiene el texto de la tarea.

```python
            tarea_completada = "1" if elemento_lista.font().strikeOut() else "0"
```

Comprueba si la tarea está tachada. Si está tachada, guarda `"1"`; si no, guarda `"0"`.

```python
            texto_archivo.write(f"{texto}|{tarea_completada}\n")
```

Escribe la tarea en el archivo con el formato `texto|estado`. `\n` agrega un salto de línea.

## Función `eliminar_tarea`

```python
def eliminar_tarea():
```

Define la función utilizada para eliminar una tarea seleccionada.

```python
    elemento_lista = lista_tareas.currentItem()
```

Obtiene la tarea que el usuario ha seleccionado actualmente.

```python
    if elemento_lista:
```

Comprueba si realmente existe una tarea seleccionada.

```python
        indice_elemento_lista = lista_tareas.row(elemento_lista)
```

Obtiene la posición de la tarea dentro de la lista.

```python
        lista_tareas.takeItem(indice_elemento_lista)
```

Elimina la tarea de la lista visual.

```python
        guardar_tareas()
```

Guarda el archivo sin la tarea eliminada.

```python
    else:
```

Se ejecuta si el usuario no seleccionó ninguna tarea.

```python
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una tarea")
```

Muestra una advertencia solicitando seleccionar una tarea.

## Función `completar_tarea`

```python
def completar_tarea():
```

Define la función que marca una tarea como completada o pendiente.

```python
    elemento_lista = lista_tareas.currentItem()
```

Obtiene la tarea seleccionada.

```python
    if elemento_lista:
```

Comprueba que exista una tarea seleccionada.

```python
        fuente = elemento_lista.font()
```

Obtiene la fuente actual de la tarea.

```python
        completado = not fuente.strikeOut()
```

Invierte el estado actual. Si la tarea no estaba tachada, pasa a estar completada; si estaba tachada, vuelve a estar pendiente.

```python
        fuente.setStrikeOut(completado)
```

Aplica el nuevo estado de tachado a la fuente.

```python
        elemento_lista.setFont(fuente)
```

Actualiza visualmente la fuente de la tarea.

```python
        elemento_lista.setForeground(QBrush(QColor("gray") if completado else QColor("black")))
```

Cambia el color del texto: gris si está completada y negro si está pendiente.

```python
        guardar_tareas()
```

Guarda el nuevo estado en `tareas.txt`.

```python
    else:
```

Se ejecuta si no existe una tarea seleccionada.

```python
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una tarea")
```

Muestra una advertencia indicando que se debe seleccionar una tarea.

## Creación de la aplicación

```python
app = QApplication(sys.argv)
```

Crea la aplicación PyQt6 y le entrega los argumentos recibidos desde el sistema.

```python
ventana = QWidget()
```

Crea la ventana principal.

```python
ventana.setWindowTitle("Lista de Tareas")
```

Establece el título de la ventana.

```python
ventana.setGeometry(100, 100, 400, 500)
```

Define la posición y el tamaño de la ventana:

- `100`: posición horizontal.
- `100`: posición vertical.
- `400`: ancho.
- `500`: alto.

## Diseño de la ventana

```python
layout_principal = QVBoxLayout()
```

Crea un diseño vertical para colocar los componentes uno debajo de otro.

```python
tareas_input_text = QLineEdit()
```

Crea el campo donde el usuario escribirá una nueva tarea.

```python
tareas_input_text.setPlaceholderText("Escribe una nueva tarea")
```

Muestra un texto de ayuda dentro del campo mientras está vacío.

```python
layout_principal.addWidget(tareas_input_text)
```

Añade el campo de texto al diseño principal.

```python
botones_layout = QHBoxLayout()
```

Crea un diseño horizontal para colocar los botones en la misma fila.

### Botón Agregar

```python
btn_agregar = QPushButton("Agregar")
```

Crea un botón con el texto `Agregar`.

```python
btn_agregar.clicked.connect(agregar_tarea)
```

Conecta el evento de clic del botón con la función `agregar_tarea`.

```python
botones_layout.addWidget(btn_agregar)
```

Añade el botón al diseño horizontal.

### Botón Eliminar

```python
btn_eliminar = QPushButton("Eliminar")
```

Crea el botón para eliminar tareas.

```python
btn_eliminar.clicked.connect(eliminar_tarea)
```

Indica que, al pulsarlo, se ejecutará `eliminar_tarea`.

```python
botones_layout.addWidget(btn_eliminar)
```

Añade el botón al diseño horizontal.

### Botón Completar

```python
btn_completar = QPushButton("Completar Tarea")
```

Crea el botón para cambiar el estado de una tarea.

```python
btn_completar.clicked.connect(completar_tarea)
```

Conecta el botón con la función `completar_tarea`.

```python
botones_layout.addWidget(btn_completar)
```

Añade el botón al diseño horizontal.

```python
layout_principal.addLayout(botones_layout)
```

Añade el grupo horizontal de botones al diseño principal.

## Lista de tareas y ejecución

```python
lista_tareas = QListWidget()
```

Crea la lista visual donde aparecerán las tareas.

```python
layout_principal.addWidget(lista_tareas)
```

Añade la lista al diseño principal.

```python
ventana.setLayout(layout_principal)
```

Asigna el diseño principal a la ventana.

```python
cargar_tareas()
```

Carga las tareas guardadas en `tareas.txt` cuando se inicia el programa.

```python
ventana.show()
```

Muestra la ventana en pantalla.

```python
sys.exit(app.exec())
```

Inicia el ciclo de eventos de PyQt6. Este ciclo permite que la aplicación detecte clics, reciba texto y responda a las acciones del usuario. Cuando la ventana se cierra, el programa termina correctamente.

## Flujo completo del programa

1. Se inicia la aplicación.
2. Se crea la ventana principal.
3. Se cargan las tareas desde `tareas.txt`.
4. El usuario puede agregar, eliminar o completar tareas.
5. Cada cambio se guarda inmediatamente.
6. Al volver a abrir el programa, las tareas conservan su estado.
