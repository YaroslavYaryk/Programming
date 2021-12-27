import socket
import threading

HOST = "127.0.0.1"
PORT = 9300

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nicknames.pop(nicknames[index])
            break


def recieve():
    while True:
        client, addr = server.accept()
        clients.append(client)

        nickname = client.send("NICK".encode('utf_8'))
        nicknames.append(nickname)

        broadcast(f"{nickname} connected to the server\n".encode('utf_8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running...")
recieve()
