import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7888))
sock.settimeout(5)  # if nobody connects it'll be error
# sock.settimeout(0) -> sock.setblocking(False)
# sock.settimeout(None) -> sock.setblocking(True)
sock.listen(5)

try:
	client, addr = sock.accept()
except socket.error:  # handle it here
	print("No connection")
else:
	result = client.recv(1024)
	print(f"result = {result.decode('utf_8')}")
	client.close()
