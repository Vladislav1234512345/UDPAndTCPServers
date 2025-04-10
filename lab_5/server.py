import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_ADDRESS = ('', 8888)

server.bind(SERVER_ADDRESS)
server.listen(5)

while True:
    print("Ожидание сообщения клиента...")
    client_socket, client_address = server.accept()
    print("Получен запрос на соединение с %s" % str(client_address))
    data = client_socket.recv(4096).decode('utf-8')
    print("Клиент %s отправил следующее сообщение: %s" % (client_address, data))
    current_time_str = time.ctime(time.time()) + '\n'
    client_socket.send(current_time_str.encode('utf-8'))
    client_socket.close()
