import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
	
	def handle(self):
		data = self.rfile.readline().strip()
		print('Got {}'.format(data))
		self.request.sendall('Hello World!')

if __name__ == '__main__':
	HOST, PORT = 'localhost', 6000

	server = socketserver.TCPServer((HOST, PORT), /*My*/TCPHandler)
	server.serve_forever()
