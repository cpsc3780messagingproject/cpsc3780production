##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   client.py:
#       Client object which contains all relevant functions for using Seiren
#       in client mode.
##############################################################################

import time
import socket
import pickle
import threading
from modules.message import Message
from modules.message_factory import construct_message

"""class sendThread (threading.thread):
    def __init__(self, clientsocket, server, sequence, id):
        self.clientsocket = clientsocket
        self.server = server
        self.sequence = sequence
        self.id = id
        
    def run(self):
    
class getThread (threading.thread):
    def __init__(self, socket, server, id):
    
    def run(self):"""

class MessageClient():
    def __init__(self, server):
        self.messages = []
        self.host = server
        self.mess_seq = 0
        self.id = 0
    
    def activate(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while True:
            if (self.id == 0):
                wrapped_msg = construct_message(6, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                data, catchgarbage = s.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                self.id = unpickled_data.destination
                print("Your assigned ID is: ", self.id)
                wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                data, catchgarbage = s.recvfrom(65536)
                print("check")
                unpickled_data = pickle.loads(data)
                wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                print("Userlist: ", unpickled_data.payload)
                
            raw_msg = raw_input("Please input a message to transmit: ")
            wrapped_msg = construct_message(1, self.mess_seq, self.id, 0, raw_msg) 
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
