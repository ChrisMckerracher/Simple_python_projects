import socket
import sys

server_address = './_socket'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('connecting to %s' % server_address)

try:
    sock.connect(server_address)
    
    message = 'Hi!'
    message = bytes(message, "utf-8")
    print('sending %s' % message)
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('recieved %s' % data)
    
    print('closing socket')
    sock.close()

except socket.error:
    print('socket error occured')
    sys.exit(1) 
