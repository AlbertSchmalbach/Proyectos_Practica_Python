import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QGridLayout
)

def crear_calculadora():
    ventana = QWidget()
    ventana.setWindowTitle('Calculadora')
    ventana.setGeometry(100, 100, 300, 400)

    layaout_principal = QVBoxLayout()

    caja_texto = QLineEdit()
    caja_texto.setReadOnly(True)
    caja_texto.setStyleSheet('font-size:28px;')

    layaout_principal.addWidget(caja_texto)

    layaout_botones = QGridLayout()

    botones = [
        ('7', 0,0), ('8', 0,1), ('9', 0,2), ('/', 0,3),
        ('4', 1,0), ('5', 1,1), ('6', 1,2), ('*', 1,3),
        ('1', 2,0), ('2', 2,1), ('3', 2,2), ('-', 2,3),
        ('0', 3,0), ('.', 3,1), ('C', 3,2), ('+', 3,3),
        ('=', 4,0, 1, 4)
    ]

    for texto, fila, columna, *detalle in botones:

        btn = QPushButton(texto)
        btn.setStyleSheet('font-size:18px')
        
        if detalle:
            layaout_botones.addWidget(btn, fila, columna, *detalle)
        else:
            layaout_botones.addWidget(btn, fila, columna)

        btn.clicked.connect(lambda _, t=texto : on_click(t, caja_texto))

    layaout_principal.addLayout(layaout_botones)
    ventana.setLayout(layaout_principal)
    ventana.show()

    return ventana


def on_click(texto, caja_texto_objects):
    if texto == 'C':
        caja_texto_objects.clear()
    elif texto == '=':
        try:
            resultado = eval(caja_texto_objects.text())
            caja_texto_objects.setText(str(resultado))
        except Exception:
            caja_texto_objects.setText("Error en el calculo")
    else:
        caja_texto_objects.setText(caja_texto_objects.text() + texto)


app = QApplication(sys.argv)
ventana = crear_calculadora()
sys.exit(app.exec())