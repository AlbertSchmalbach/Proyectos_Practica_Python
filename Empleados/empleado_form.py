import pandas as pd
import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView
)

df = pd.DataFrame(columns=["Nombre", "Apellido", "Profesion", "Sueldo", "Sueldo Neto"] )

def crear_app():
    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle("Registro de Empleado")
    ventana.resize(800, 600)

    # Ventana principal
    layaout_principal = QVBoxLayout()
    layaout_principal.addSpacing(30)

    # Layaout de formulario
    layaout_form=QHBoxLayout()

    # Nombre
    nombre_input = QLineEdit()
    nombre_input.setFixedHeight(40)
    nombre_input.setPlaceholderText("Nombre")
    layaout_form.addWidget(nombre_input)

    # Apellido
    ape_input = QLineEdit()
    ape_input.setFixedHeight(40)
    ape_input.setPlaceholderText("Apellido")
    layaout_form.addWidget(ape_input)

    # Profesion
    profe_input = QLineEdit()
    profe_input.setFixedHeight(40)
    profe_input.setPlaceholderText("Profesion")
    layaout_form.addWidget(profe_input)

    # Sueldo
    sueldo_input = QLineEdit()
    sueldo_input.setFixedHeight(40)
    sueldo_input.setPlaceholderText("Sueldo")
    layaout_form.addWidget(sueldo_input)

    layaout_principal.addLayout(layaout_form)

    # Botones
    layaout_btns = QHBoxLayout()

    btn_agregar = QPushButton("Agregar")
    btn_agregar.setFixedHeight(40)
    layaout_btns.addWidget(btn_agregar)

    btn_exportar = QPushButton("Exportar Excel")
    btn_exportar.setFixedHeight(40)
    layaout_btns.addWidget(btn_exportar)

    layaout_principal.addLayout(layaout_btns)

    # tabla
    tabla=QTableWidget()
    tabla.setColumnCount(5)
    tabla.setHorizontalHeaderLabels(["Nombre", "Apellido", "Profesion", "Sueldo", "Sueldo Neto"])

    tabla.horizontalHeader().setStretchLastSection(True)
    tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    layaout_principal.addWidget(tabla)

    ventana.setLayout(layaout_principal)
    ventana.show()
    

    # Agregar datos
    def agregar_datos():
        nombre=nombre_input.text()
        apellido=ape_input.text()
        profesion=profe_input.text()
        sueldo=sueldo_input.text()
        sueldo=float(sueldo)

        if sueldo > 0 and sueldo <=1000:
            sueldo_neto=sueldo*0.8
        elif sueldo>1000 and sueldo<=4000:
            sueldo_neto=sueldo*0.75
        else:
            sueldo_neto=sueldo*0.65

        nueva_fila={"Nombre":nombre,
                    "Apellido":apellido,
                    "Profesion":profesion,
                    "Sueldo":sueldo,
                    "Sueldo Neto":sueldo_neto}

        global df
        df.loc[len(df)] = nueva_fila

        fila = tabla.rowCount()
        tabla.insertRow(fila)
        tabla.setItem(fila, 0, QTableWidgetItem(nombre))
        tabla.setItem(fila, 1, QTableWidgetItem(apellido))
        tabla.setItem(fila, 2, QTableWidgetItem(profesion))
        tabla.setItem(fila, 3, QTableWidgetItem(f"{sueldo:.2f}"))
        tabla.setItem(fila, 4, QTableWidgetItem(f"{sueldo_neto:.2f}"))

        tabla.resizeRowsToContents()

        nombre_input.clear()
        ape_input.clear()
        profe_input.clear()
        sueldo_input.clear()

    def exportar_excel():
        if os.path.exists('data_empleado.xlsx'):
            os.remove('data_empleado.xlsx')

        df.to_excel('data_empleado.xlsx', index=False, engine='openpyxl')

    btn_exportar.clicked.connect(exportar_excel)
    btn_agregar.clicked.connect(agregar_datos)
    sys.exit(app.exec_())

crear_app()