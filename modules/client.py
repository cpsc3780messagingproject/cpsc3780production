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
from message import Message

class MessageClient():
    def __init__(self, server):
        self.messages = []
        self.host = server
        self.mess_seq = 0
        
        random.seed(None)
        self.id
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            #s.setdefaulttimeout(5)
            s.connect(self.host)
            clientid = pickle.loads(s.recv(65536))#receive ID from server
            print ("Your assigned ID is: ", clientid.payload())
            self.id = clientid.payload()
            userlist = pickle.loads(s.recv(65536))#receive and print the user list
            print("Userlist: ", userlist.payload())
            
            

    def construct_message(self, message_type, message, target):
        seq_str = '{:0>3}'.format(self.mess_seq)
        id_str = '{:0>10}'.format(self.id)
        target_str = '{:0>10}'.format(target)
        new_message = Message(seq_str, message_type, id_str, target_str, 
                              message)
        return new_message

    def send(self, message, target):
        pickled_message = pickle.dumps(message,-1)
        socket.send(pickled_message)
