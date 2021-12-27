import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("localhost", 5000))
sock.listen()


while True:
    print("before .accept")
    client, addr = sock.accept()
    print(f"Connected from {addr}")

    while True:
        message = client.recv(4096)
        if not message:
            break
        else:
            response = "hello world\n"
            client.send(response.encode('utf_8'))
