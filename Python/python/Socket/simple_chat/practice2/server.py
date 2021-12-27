import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 9998

sock.bind((HOST, PORT))
sock.listen()

clients = []
nicknames = []


def broadcast(message):
	for client in clients:
		client.send(message)


def handle(client):
	while True:
		try:
			message = client.recv(1024).decode('utf_8')
			broadcast(message.encode('utf_8'))
		except Exception:
			index = clients.index(client)
			clients.remove(clients[index])
			nicknames.remove(nicknames[index])
			client.close()
			break


def recieve():
	print("Start server...")
	while True:
		client, addr = sock.accept()
		clients.append(client)

		nickname = client.send("NICK".encode('utf_8'))
		nicknames.append(nickname)

		broadcast(f"{nickname} Connected to Server\n".encode('utf_8'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()


recieve()