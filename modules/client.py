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
import stringIO
from message import Message

class MessageClient():
    def __init__(self, port):
        self.messages = []
        self.host = ''
        self.port = port
        self.mess_seq = 0
        
        random.seed(None)
        self.id = randint(1, 1000000000)
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))

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
        
