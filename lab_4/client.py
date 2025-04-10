import socket


SERVER_ADDRESS = ('localhost', 15253)

client_socket = socket.socket()

client_socket.connect(SERVER_ADDRESS)
text = str(input("Введите сообщение серверу: "))
client_socket.send(text.encode('utf-8'))
data = client_socket.recv(4096)
print(data.decode('utf-8'))
