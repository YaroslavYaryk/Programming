import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8888))

try:
	result = sock.recv(1024)
except KeyboardInterrupt:
	sock.close()
else:
	print(f"result - {result.decode('utf_8')}")
