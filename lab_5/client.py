import socket


SERVER_ADDRESS = ('localhost', 8888)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)
text = str(input("Введите сообщение серверу: "))
client_socket.send(text.encode('utf-8'))
current_time = client_socket.recv(1024)
client_socket.close()
print("Текущее время: %s" % current_time.decode('utf-8'))

