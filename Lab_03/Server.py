__author__ = 'Arkadiusz'

import socket
import sys

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('localhost', 10001)
print >>sys.stderr, 'Starting up on %s port %s' % server_address
sock.bind(server_address)

#listen for incoming connections
sock.listen(1)

while True:
    # wait for connection
    print >>sys.stderr, 'Waiting for connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'Connection from ', client_address

        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(100)
            print >>sys.stderr, 'Received "%s"' % data
            if data:
                print >>sys.stderr, 'Sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'No more data from ', client_address
                break

    finally:
        # Clean up the connection
        connection.close()