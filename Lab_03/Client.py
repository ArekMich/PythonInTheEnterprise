__author__ = 'Arkadiusz'

import socket
import sys
import ParseConfig
import Main

# tictactoe = Main
# config = ParseConfig()
tictactoe = Main.TicTacToe()#config)
# tictactoe.play()

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print >>sys.stderr, 'Connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # send data
    # message = 'This is the message. It will be repeated.'
    # print >>sys.stderr, 'Sending "%s"' % message
    sock.sendall(tictactoe.play())
    data = sock.recv(100)
    print >>sys.stderr, 'Received "%s"' % data
    #look for the response
    # amount_received = 0
    # amount_expected = len(message)
    #
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print >>sys.stderr, 'Received "%s"' % data

finally:
    print >>sys.stderr, 'Closing socket'
    sock.close()
