import socket
import os


soket_name = "unix.sock"
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)


if os.path.exists(soket_name):
	os.remove(soket_name)


sock.bind(soket_name)

while True:
	try:
		result = sock.recv(1024)
	except KeyboardInterrupt:
		sock.close()
	else:
		print(f"Message - '{result.decode('utf_8')}' ")
