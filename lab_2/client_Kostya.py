import time
import socket

host = 'localhost'
port = 20001
serverAddressPort = (host, port)
print('serverAddressPort=', serverAddressPort,
      type(serverAddressPort))
bufferSize = 1024
UDPClientSocket = socket.socket(socket.AF_INET,
                                socket.SOCK_DGRAM)
count = 0
while True:
    try:
        count += 1
        z = 'Привет UDP сервер! Я Костик! Сколько времени?' + str(count)
        print('z=', z)
        UDPClientSocket.sendto(z.encode(), serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = msgFromServer[0].decode()
        print('Получено от сервера:', msg)
        time.sleep(3)
    except KeyboardInterrupt():
        UDPClientSocket.close()
        break

UDPClientSocket.close()
