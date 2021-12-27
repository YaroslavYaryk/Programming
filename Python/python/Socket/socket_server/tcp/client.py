import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 7000))
sock.send(b"New dmadk;l")
result = sock.recv(64)
print(f"Response - {result}")
sock.close()