import socket
from time import sleep


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind(("127.0.0.1", 7777))
	sock.listen(5)
	sock.setblocking(False)
	while True:
		try:
			client, addr = sock.accept()
		except (KeyboardInterrupt, socket.error):
			print("error")
			sleep(1)
		else:
			result = client.recv(1024)
			print(f"result <--> {result.decode('utf_8')} ")

