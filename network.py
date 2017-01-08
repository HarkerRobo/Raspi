import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
	
	def handle(self):
		data = self.request.recv(1024).strip()
		print('Got {}'.format(data))
		self.request.sendall(b'Hello World!')

if __name__ == '__main__':
	HOST, PORT = '0.0.0.0', 6000

	server = socketserver.TCPServer((HOST, PORT), TCPHandler)
	server.serve_forever()
