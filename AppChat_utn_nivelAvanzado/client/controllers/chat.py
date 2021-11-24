from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt

from views.chat import ChatForm
from controllers.login import LoginWindow

import socket
import threading

class ChatWindow(QWidget, ChatForm):

    def __init__(self, username, token):
        super().__init__()
        
        self.username = username
        self.token = 0x85A4
        self.setupUi(self)

        self.connect()

        self.sendButton.clicked.connect(self.send_messages)

    def hexa_to_byte(self):
        self.token_byte = bytearray(self.token.to_bytes(2, "big"))

    def connect(self):
        connection_data = ('127.0.0.1', 55555)
        af_inet = socket.AF_INET
        sock_stream = socket.SOCK_STREAM

        self.client = socket.socket(af_inet, sock_stream)
        self.client.connect(connection_data)

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        self.hexa_to_byte()
        self.client.send(self.token_byte)
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
                import operator
                print(type(message))
                print(message)

                if operator.contains(message,"@tokenhexa"):
                    pass
                elif operator.contains(message,"@usernameConnected to server"):
                    self.chatTextEdit.append("Connected to server")
                    self.chatTextEdit.setAlignment(Qt.AlignLeft)
                else:
                    self.chatTextEdit.append(message)
                    self.chatTextEdit.setAlignment(Qt.AlignLeft)
            except:
                self.client.close()
                break
    
    def send_messages(self):
        message = self.messageLineEdit.text()

        message1 = f"{self.username}: {message}"
        my_message = f"{message}"
        self.client.send(message1.encode('utf-8'))
        self.chatTextEdit.append(my_message)
        self.chatTextEdit.setAlignment(Qt.AlignRight)
        self.messageLineEdit.clear()