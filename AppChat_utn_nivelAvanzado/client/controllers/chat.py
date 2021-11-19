from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading

class ChatWindow(QWidget, ChatForm):

    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setupUi(self)

        self.connect()

        self.sendButton.clicked.connect(self.send_messages)

    def connect(self):
        connection_data = ('127.0.0.1', 55555)
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM

        self.client = socket.socket(af_inet, sock_stream)
        self.client.connect(connection_data)

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        self.client.send(self.username.encode('utf-8'))
        self.logoutButton.clicked.connect(self.logout)
    
    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.client.close()
        self.close()

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chatTextEdit.append(message)
                self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.client.close()
                break
    
    def send_messages(self):
        message = self.messageLineEdit.text()

        message = f"{self.username}: {message}"
        self.client.send(message.encode('utf-8'))
        self.chatTextEdit.append(message)
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        self.messageLineEdit.clear()