import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_item = [
	"GET / HTTP/1.1",
	"HOST: example.com",
	"Connection: keep-alive",
	"Accept: text/html",
	"\n"
]

content = "\n".join(content_item)
print("---HTTP MESSAGE---")
print(content)
print("---END OF MESSAGE---")
sock.send(content.encode())
result = sock.recv(10024)
print(result.decode())