from PySide2.QtWidgets import QApplication
from controllers.login import LoginWindow
from pathlib import Path
from PySide2.QtGui import QIcon

import sys

if __name__ == '__main__':
    ruta_icono = Path('.', 'assets', 'logo.png')
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.setWindowTitle('UTN CHAT')
    window.setWindowIcon(QIcon(str(ruta_icono)))
    window.setFixedSize(316, 242)
    window.show()
    app.exec_()