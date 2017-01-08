import socket, select, threading, time

HOST = '0.0.0.0' # For accepting connections from any device
PORT = 6000
BACKLOG = 5 # Maximum number of clients
SIZE = 1024 # Maximum message size

# Create the socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(BACKLOG)
clients = [s]

# Sends message to all clients
def broadcast(message):
	for i in clients:
		if i is not s:
			i.send(message)

# When the server accepts data
def newMessage(socket, data):
	print('Got {}'.format(data))
	broadcast(data)

def AcceptClients():
	while True:
		# See if there is any activity
		inputReady, outputReady, exceptREady = select.select(clients, [], [])
		for x in inputReady:
			if x == s:
				# Client has connected to the server
				csock, addr = s.accept()
				clients.append(csock)

			else:
				# A client did something
				data = x.recv(SIZE)
				if data:
					# Client has sent something
					newMessage(x, data)
				else:
					# Client has disconnected
					x.close()
					clients.remove(x)

# Run the client-accepting routine as a thread
acceptThread = threading.Thread(target=AcceptClients, args=[])
acceptThread.start()

try:
	while True:
		broadcast(b'hi\n')
		time.sleep(1)
except:
	pass
finally:
	s.close()
