import sys
import os

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QHBoxLayout, QListWidgetItem
)

from PyQt6.QtGui import QFont, QBrush, QColor

archivo = "tareas.txt"

def cargar_tareas():
    if  os.path.exists(archivo):
        with open(archivo, 'r', encoding="utf-8") as contenido_archivo:
            for linea in contenido_archivo:
                tarea, estado_tarea = linea.strip().split("|")

                elemento_lista = crear_elemento_lista_widget(tarea, estado_tarea == "1")

                lista_tareas.addItem(elemento_lista)

def crear_elemento_lista_widget(texto, completado=False):
    elemento_lista = QListWidgetItem(texto)
    fuente = QFont()
    fuente.setStrikeOut(completado)
    elemento_lista.setFont(fuente)

    if completado:
        elemento_lista.setForeground(QBrush(QColor("gray")))
    
    return elemento_lista

def agregar_tarea():
    texto = tareas_input_text.text().strip()
    if texto:
        elemento_lista = crear_elemento_lista_widget(texto)
        lista_tareas.addItem(elemento_lista)
        tareas_input_text.clear()
        guardar_tareas()
    else:
        QMessageBox.warning(ventana, "Advertencia", "Escribe una tarea...")

def guardar_tareas():
    with open(archivo, "w", encoding="utf-8") as texto_archivo:
        for elemento_lista_indice in range(lista_tareas.count()):
            elemento_lista = lista_tareas.item(elemento_lista_indice)
            texto = elemento_lista.text()
            tarea_completada = "1" if elemento_lista.font().strikeOut() else "0"
            texto_archivo.write(f"{texto}|{tarea_completada}\n")

def eliminar_tarea():
    elemento_lista = lista_tareas.currentItem()
    if elemento_lista:
        indice_elemento_lista = lista_tareas.row(elemento_lista)
        lista_tareas.takeItem(indice_elemento_lista)
        guardar_tareas()
    else:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una tarea")

def completar_tarea():
    elemento_lista = lista_tareas.currentItem()
    if elemento_lista:
        fuente = elemento_lista.font()
        completado = not fuente.strikeOut()
        fuente.setStrikeOut(completado)
        elemento_lista.setFont(fuente)
        elemento_lista.setForeground(QBrush(QColor("gray") if completado else QColor("black")))
        guardar_tareas()
    else:
        QMessageBox.warning(ventana, "Advertencia", "Selecciona una tarea")

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Lista de Tareas")
ventana.setGeometry(100, 100, 400, 500)

layout_principal = QVBoxLayout()

tareas_input_text =QLineEdit()
tareas_input_text.setPlaceholderText("Escribe una nueva tarea")
layout_principal.addWidget(tareas_input_text)

botones_layout = QHBoxLayout()

btn_agregar = QPushButton("Agregar")
btn_agregar.clicked.connect(agregar_tarea)
botones_layout.addWidget(btn_agregar)

btn_eliminar = QPushButton("Eliminar")
btn_eliminar.clicked.connect(eliminar_tarea)
botones_layout.addWidget(btn_eliminar)

btn_completar = QPushButton("Completar Tarea")
btn_completar.clicked.connect(completar_tarea)
botones_layout.addWidget(btn_completar)

layout_principal.addLayout(botones_layout)

lista_tareas = QListWidget()
layout_principal.addWidget(lista_tareas)

ventana.setLayout(layout_principal)

cargar_tareas()

ventana.show()

sys.exit(app.exec())

