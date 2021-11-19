import socket
import threading


host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #el primer argumento significa que vamos a usar un socket tipo internet que significa que vamos a utilizar como direccion el host y el port
    #el segundo argumento indica que vamos a usar el protocolo tcp

server.bind((host, port))
    #bind sirve para pasarle los datos de conexion que va a tener el servidor en formato de tupla
server.listen()
    #le decimos que este a la escucha de las conexiones
print(f"Server running on {host}:{port}")


clients = []
usernames =[]

def broadcast(message, _client):#el guion bajo en el parametro es para diferenciarlo de la variable
    #sera la funcion encargada de enviar el mensaje a todos los participantes
    for client in clients:
        #por cada cliente en la lista clientes
        if client != _client:
            #excepto el cliente que lo envio
            client.send(message)
                #vamos a enviar ese mensaje

def disconnected_client(client):
    index = clients.index(client)
        #la funcion index trae la posicion del cliente
    username = usernames[index]
        #el username lo obtenemos gracias a que al agregar al mismo tiempo el cliente y el username ambos tendran la misma posicion en sus respectivas listas
    broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
        #enviamos de parte del servidor un mensaje a los clientes notificando la desconexion 
        #como no podemos enviar el string directamente tenemos que pasarlo a byte y para esto se utiliza un sistema de codificacion en este caso utf-8 con la funcion encode
    clients.remove(client)
        #con remove borramos el cliente de la lista
    usernames.remove(username)
        #borramos el username de la lista
    client.close()
        #cerramos la conexion con ese cliente
    print(f"{username} disconnected")

def handle_messages(client):
    #creamos la funcion para poder manejar los mensajes de cada cliente
    while True:
        #creamos un loop infinito para que este a la escucha siempre
        try:
            message = client.recv(1024)
                #obtenemos el mensaje de ese cliente.
                #el objeto de la conexion tiene una funcion que se llama recive abreviado, dentro del parentecis colocamos 1024(bytes) ese sera el limite que la funcion podra leer 
                #la funcion retorna el mensaje
            broadcast(message, client)
                #hacemos el broadcast de ese mensaje 
        except:
            disconnected_client(client)
            break
                #al ocurrir un error rompe el loop

def receive_connections():
    #con esta funcion el servidor va a poder aceptar y manejar las conexiones 
    while True:
        #creamos el loop 
        client, address = server.accept()
            #el socket que lo pusimos como "server" tiene una funcion accept que acepta las conexiones que se conectes a los datos de conexion que pusimos arriba (host,port)
            #esta funcion retorna dos datos, el ip y el puerto de donde se conectan los clientes

        client.send("@username".encode("utf-8"))
            #enviamos un mensaje a la aplicacion del cliente para pedirle el username
            #encode lo usamos para poder enviar el mensaje en bytes
        username = client.recv(1024).decode('utf-8')
            #el mensaje que recibimos lo decodificamos con la funcion decode en el mismo formato que se envio (utf8)

        clients.append(client)
        usernames.append(username)
            #agregamos el cliente y el username a dichas listas

        print(f"{username} is connected with {str(address)}")
            #imprimimos el mensaje de conexion en la consola del servidor para guiarnos por donde va el codigo

        message = f"ChatBot: {username} joined the chat!".encode("utf-8")
            #creamos un mensaje para enviar a los clientes de conexion nueva
        broadcast(message, client)
            #enviamos el mensaje a todos los clientes
        client.send("Connected to server".encode("utf-8"))
            #enviamos un mensaje solo al cliente nuevo para avisarle que se conecto al servidor

        thread = threading.Thread(target=handle_messages, args=(client,))
            #creamos un hilo, con target especificamos la funcion y como toma argumento vamos a pasarle los argumentos con args=
            #como es una tupla con un solo valor hay que ponerle la , para evitar el error
        thread.start()
            #iniciamos el hilo

receive_connections()