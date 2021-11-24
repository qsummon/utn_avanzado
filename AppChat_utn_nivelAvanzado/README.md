# UTN CHAT
Aplicación desarrollada para entrega final de Python nivel Avanzado
Universidad UTN  

## Integrantes del equipo
Federico Daniel Ara  
Marcelo Fabian Zurita  

## Github Link
https://github.com/qsummon/utn_avanzado

## Descripción
UTN_CHAT es una aplicacion desarrollada en python 3.x
La aplicación permite "chatear" entre usuarios y cumple con las premisas
requeridas (https://campus.utnba.centrodeelearning.com/mod/assign/view.php?id=1032059)

La aplicación loguea actividad tanto en la consola(terminal) como archivo log (utn_chat_info.log)

## Detalle de Requesitos
```
      PRIMERA APP: server.py ==> Cumplido
      SEGUNDA APP: cliente.py ==> Cumplido
      1) 2 app Una con las funcionalidades y la otra para comunicarme desde fuera de la
         primera app (puede ser por consola) ==> Cumplido
      2) Realizado en python puro, tkinter o pyqt ==> Cumplido (pyqt)
      3) Patrón MVC ==> Cumplido
      4) POO  ==> Cumplido
      5) Observador de eventos con (decorador o un Patrón Observer)
         que registre en una tabla de log (la fecha, descripción, otro dato)
          ==> Cumplido (funcion my_logger con decorador)
          ==> Registra en archivo log utn_chat_info.log
      6) La información enviada desde la app cliente de viajar como bytearray
         conteniendo hexadecimales y la app "server" debe poder responderle.
         https://docs.python.org/es/3/library/socket.html
        ==> Cumplido
```

## IMPORTANTE
```
La aplicacion toma como "server" la IP local del equipo
En caso de querer correrla en una LAN desde distintos equipos se debe
indicar el server en el ejecutable chat.py

  host = socket.gethostbyname(socket.gethostname())

  reemplazar por la IP donde se ejecute el server
```

## Requirements
```
python 3.6 o superior  

Package             Version  
------------------- --------
pys2-msgboxes       0.0.2
PySide2             5.15.2
shiboken2           5.15.2
```

## Instalacion de ambiente virtual
```
pip install -r requirements.txt
```

## Platforms
```
- Windows 10
- LINUX
```

## Uso:
```
Una vez instalado python y sus dependencias se debe:
Ejecutar el server
cd AppChat_utn_nivelAvanzado
python server.py

Ejecutar el cliente
cd AppChat_utn_nivelAvanzado/client
python client.py
```

## Autores
* ** Federico Daniel Ara
* ** Marcelo Fabian Zurita
