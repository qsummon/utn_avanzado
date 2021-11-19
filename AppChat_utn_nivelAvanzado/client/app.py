from PySide2.QtWidgets import QApplication
from controllers.login import LoginWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()

    window.show()
    app.exec_()