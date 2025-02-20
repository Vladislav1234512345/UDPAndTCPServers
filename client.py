import socket
# данные сервера
host = 'localhost'
port = 20001
serverAddressPort = (host, port)
print('serverAddressPort=',serverAddressPort,
      type(serverAddressPort))
bufferSize = 1024

UDPClientSocket=socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)

send_message = str(input("Введите текст: "))
UDPClientSocket.sendto(send_message.encode(),serverAddressPort)
# UDPClientSocket.sendto(b'Привет',serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom (bufferSize)
msg=msgFromServer [0]
print('Получено от сервера:', msg.decode())
UDPClientSocket.close()