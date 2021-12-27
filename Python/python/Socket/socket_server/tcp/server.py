import socketserver


class EchoTCPServer(socketserver.BaseRequestHandler):

	def handle(self):
		data = self.request.recv(1024).strip()
		print(f"Address - {self.client_address[0]}")
		print(f"Data - {data.decode()}")
		self.request.sendall(data)


if __name__ == "__main__":
	with socketserver.TCPServer(("0", 7000), EchoTCPServer) as server:
		server.serve_forever()