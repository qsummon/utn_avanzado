from PySide2.QtWidgets import QWidget
from views.login import LoginForm

from pys2_msgboxes import msgboxes

class LoginWindow(QWidget, LoginForm):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.joinButton.clicked.connect(self.join_to_chat)

    def join_to_chat(self):
        username = self.usernameLineEdit.text()
        token = 0x85A4
        if username != '':
            from controllers.chat import ChatWindow
            self.chat_window = ChatWindow(username, token)
            self.chat_window.show()
            self.close()
        else:
            msgboxes.input_error_msgbox('Dato requerido', 'Debe introducir un username')
