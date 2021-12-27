import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8000))
sock.listen(5)
sock.settimeout(5)

try:
	client, addr = sock.accept()
except (socket.error, KeyboardInterrupt):
	print("Error")
else:
	result = client.recv(1024)
	print(f"Result - {result.decode('utf_8')}")
	client.close()