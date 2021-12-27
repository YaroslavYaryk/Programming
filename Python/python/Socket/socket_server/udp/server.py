import socketserver


class EchoUDPServer(socketserver.BaseRequestHandler):

	def handle(self):
		data, socket = self.request
		print(f"Address - {self.client_address[0]}")
		print(f"Data - {data.decode()}")
		socket.sendto(data, self.client_address)


if __name__ == "__main__":
	with socketserver.UDPServer(("0", 7000), EchoUDPServer) as server:
		server.serve_forever()
