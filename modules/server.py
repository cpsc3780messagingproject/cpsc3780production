##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   server.py:
#       Server object which contains all relevant functions for using Seiren 
#       in server mode.
##############################################################################

import time
import socket
import pickle
from message import Message

class MessageServer():
    def __init__(self, port):
        self.host = ''
        self.port = port
        self.rank = 0                       # Rank is used to determine which
                                            # other server the server should
                                            # talk to when updating client
                                            # lists. While it always starts at
                                            # 0, upon hooking a server into a
                                            # network, it will slot itself
                                            # into the highest open rank. 
        self.peers = set()
		self.client_list = {}
        self.messages = []
        

    def activate(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            s.listen(1)
            conn, addr = s.accept()
            # This could be understood as the 'main' function of the server.
            # Routing logic, listening, etc. will all be done when 
            # server.activate() is called. Note that the server constructs
            # its socket upon __init__ currently; I'm not sure if this is
            # actually an intelligent way to construct the class - we may
            # want to move s.bind() to server.activate().
			print 'Connected by', addr
            while 1:
                data = conn.recv()
                if not data: break
                conn.sendall(data)
            
    def receive_message(self, recvd_message):
        reconstructed_message = pickle.loads(recvd_message)
	    