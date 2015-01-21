import socket
import sys
import os

server_address = './_socket' #choose socket location

try:
    os.unlink(server_address) #remove current socket file
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) #assign sock to socket

print('starting up on %s' % server_address)
sock.bind(server_address) #bind socket to specified address

sock.listen(1) #begin socket listening

while True:
    print("waiting for connection...")
    connection, client_address = sock.accept()

    try:
        print('connection from %s ' % client_address)
        data = connection.recv(16)
        print("recieved %s" % data)
        
        if data:
            print('sending data back to the client')
            connection.sendall(data)
        else:
            print("done data")

    finally:
        connection.close()

