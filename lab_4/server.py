import socket

SERVER_ADDRESS = ('', 15253)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(SERVER_ADDRESS)

server_socket.listen(1)

print("Ожидание подключения клиента...")

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(4096).decode('utf-8')
    print("Получили сообщение от клиента:", data)
    data = data.upper()[::-1]
    client_socket.send(data.encode('utf-8'))
    client_socket.close()
