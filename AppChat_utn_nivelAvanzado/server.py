import socket
import threading
import binascii
import datetime



host = socket.gethostbyname(socket.gethostname())
port = 55555


def logtime():
    return datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'UTN Chat App log: {}'.format(args))
        return orig_func(*args, **kwargs)

    return wrapper


@ my_logger
def utn_chat_info(*args, **kwargs):
    print('INFO:Terminal Output: {}'.format(args))


#
# Inicio Main code
#
utn_chat_info(logtime(), "Iniciando Server...", "[STARTING]",
              host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

utn_chat_info(logtime(), "[SERVER] Corriendo OK!")
utn_chat_info(logtime(), "[LISTENING] Esperado Conexiones en IP:",
              host, "puerto:", port)

clients = []
usernames = []


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)


def disconnected_client(client):
    index = clients.index(client)
    username = usernames[index]
    broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
    clients.remove(client)
    usernames.remove(username)
    client.close()
    utn_chat_info(logtime(), username, "Desconectado")


def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            disconnected_client(client)
            break


def receive_connections():
    while True:
        client, address = server.accept()
        client.send("@tokenhexa".encode("utf-8"))
        token = client.recv(1024)
        token = binascii.hexlify(token).decode('utf-8')
        utn_chat_info(logtime(), "Client Hexadecimal token :", token)

        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        utn_chat_info(logtime(), "user id: ", username, "Conectado OK")
        utn_chat_info(logtime(), "[CONEXIONES ACTIVAS]",
                      threading.activeCount())
        message = f"ChatBot: {username} joined the chat!".encode("utf-8")
        broadcast(message, client)
        client.send("Connected to server".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()


receive_connections()
