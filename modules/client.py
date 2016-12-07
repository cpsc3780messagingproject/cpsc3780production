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

class MessageClient():
    def __init__(self, server):
        self.messages = []
        self.host = (server, 5000)
        self.mess_seq = 0
        self.id = 0
    
    def activate(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        while True:
            if (self.id == 0):
                wrapped_msg = construct_message(6, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), self.host)
                data, self.host = s.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                self.id = unpickled_data.destination
                print("Your assigned ID is: ", unpickled_data.payload)
                wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), self.host)
                data, self.host = s.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), self.host)
                print("Userlist: ", unpickled_data.payload)
                
            raw_msg = raw_input("Please input a message to transmit: ")
            wrapped_msg = construct_message(1, self.mess_seq, self.id, 0, raw_msg) 
            s.sendto(pickle.dumps(wrapped_msg), self.host)
