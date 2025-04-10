import socket
import time

host = 'localhost'
port = 20001
serverAddressPort = (host, port)
print('serverAddressPort=', serverAddressPort,
      type(serverAddressPort))
bufferSize = 1024
UDPServerSocket = socket.socket(socket.AF_INET,
                                socket.SOCK_DGRAM)
UDPServerSocket.bind(serverAddressPort)
print('Сервер запущен! Запустите клиента!')
while True:
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        clientIP = bytesAddressPair[1]
        print('clientIP=', clientIP)
        clientMsg = bytesAddressPair[0].decode()
        print('try: clientMsg=', clientMsg)
        timestr = time.ctime(time.time()) + '\r\n'
        data = clientMsg + timestr
        UDPServerSocket.sendto(data.encode(), clientIP)

    except KeyboardInterrupt:
        UDPServerSocket.close()
        break
    else:
        print('else: clientMsg=', clientMsg)

UDPServerSocket.close()

