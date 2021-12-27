import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))
result = sock.recv(1024)  # to get it here we have to send
# message from outside(from cliend (another file))
print(f"\nMessage - {result.decode('utf_8')}")
sock.close()
