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
from modules.message import Message
from modules.message_factory import construct_message

class MessageClient():
    def __init__(self, server):
        self.messages = []
        self.host = server
        self.mess_seq = 0
        self.id = 0
        
        """s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.setdefaulttimeout(5)
        raw_msg = input("Please input a message to transmit: ")
        wrapped_msg = construct_message("SND", raw_msg, 0) 
        s.sendto(pickle.dumps(wrapped_msg), (server, 5000))
        s.connect((self.host, 5000))
        clientid = pickle.loads(s.recv(65536))#receive ID from server
        print ("Your assigned ID is: ", clientid.payload())
        self.id = clientid.payload()
        userlist = pickle.loads(s.recv(65536))#receive and print the user list
        print("Userlist: ", userlist.payload())"""
    
    def activate(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.setdefaulttimeout(5)
        
        while True:
            raw_msg = input("Please input a message to transmit: ")
            wrapped_msg = construct_message("SND", self.mess_seq, self.id, 0, raw_msg) 
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
