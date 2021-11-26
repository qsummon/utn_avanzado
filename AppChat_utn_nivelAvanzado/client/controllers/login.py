from PySide2.QtWidgets import QWidget
from views.login import LoginForm
from pathlib import Path
from PySide2.QtGui import QIcon
from pys2_msgboxes import msgboxes

class LoginWindow(QWidget, LoginForm):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.joinButton.clicked.connect(self.join_to_chat)

    def join_to_chat(self):
        username = self.usernameLineEdit.text()
        token = ""
        if username != '':
            from controllers.chat import ChatWindow
            ruta_icono = Path('.', 'assets', 'logo.png')
            self.chat_window = ChatWindow(username, token)
            self.chat_window.setWindowTitle('UTN CHAT')
            self.chat_window.setWindowIcon(QIcon(str(ruta_icono)))
            self.chat_window.setFixedSize(877, 538)
            self.chat_window.show()
            self.close()
        else:
            msgboxes.input_error_msgbox('Dato requerido', 'Debe introducir un username')
