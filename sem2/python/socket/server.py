import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 12345))

s.listen(1)

print('Waiting for connection ....')

client, address = s.accept()

print('Connection stabilished with', address)

# message = 'Welcome to Your local server'.encode()
# client.send(massage)

# print(client.recv(1024).decode())

while 1:
    try:
        client.send(input('sent:').encode())
        print('recived:',client.recv(1024).decode())
    except:
        break

s.close()