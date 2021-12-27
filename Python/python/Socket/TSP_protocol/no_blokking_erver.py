import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7000))
sock.listen(5)
sock.setblocking(False)

while True:
	try:
		client, addr = sock.accept()
	except socket.error:
		print("NO cient")
		time.sleep(2)
	except KeyboardInterrupt:
		break
	else:
		sock.setblocking(True)
		result = client.recv(1024)
		print(f"Result = {result.decode('utf_8')}")
		# sock.close()
		client.close()

# print()
