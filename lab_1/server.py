import socket


TRANSLITES = {
    "а": "a",
    "е": "e",
    "и": "i",
    "о": "o",
    "у": "u",
    "э": "a",
    "ю": "yu",
    "я": "ya",
 }


# данные сервера
host = 'localhost'
port = 20001
serverAddressPort = (host, port)
print('serverAddressPort=',serverAddressPort,
      type(serverAddressPort))
# serverAddressPort= ('localhost', 20001) <class 'tuple'>

bufferSize=1024
UDPServerSocket=socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
UDPServerSocket.bind(serverAddressPort)
print('Сервер запущен! Запустите клиента!')

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
print('bytesAddressPair=', bytesAddressPair,
      type(bytesAddressPair))
# bytesAddressPair= (b'Hello', ('127.0.0.1', 58141))
# <class 'tuple'>

clientIP = bytesAddressPair [1]
print('clientIP=',clientIP, type(clientIP))
# clientIP= ('127.0.0.1', 61384) <class 'tuple'>

message=str(bytesAddressPair [0].decode())

translite_message = ""

for i in range(len(message)):
    symbol_is_uppercase = False
    if message[i].isupper():
        symbol_is_uppercase = True

    if TRANSLITES.get(message[i].lower(), None) is not None:
         translite_message += TRANSLITES[message[i].lower()] if not symbol_is_uppercase else TRANSLITES[message[i].lower()].upper()
    else:
        translite_message += message[i]

print('bytesAddressPair [0]=', translite_message)
# bytesAddressPair [0]= b'Hello'

UDPServerSocket.sendto(translite_message.encode(),clientIP)
UDPServerSocket.close()