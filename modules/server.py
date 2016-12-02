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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.setdefaulttimeout(5)
        s.bind((self.host, self.port))
        print(s.gethostname())
        s.listen(1)
        conn, addr = s.accept()
        print "Connected by ", addr
        while True:
            new_id = randint(1, 100000000)
            while True:
                if new_id in self.client_list:
                    new_id = randint(1, 1000000000)
                else:
                    break
            id_str = '{:0>10}'.format(new_id)
            self.client_list.update({'id_str': 
                                     s.gethostbyname(gethostname())})
            id_assign = construct_message("ASN", new_id, id_str)
            conn.sendto(self.pickle_message(id_assign))
            uselist_string = ""
            for key in self.client_list:
                uselist_string = uselist_string + " " + key
            uselist_message = construct_message("USR", uselist_string, id_str)
            conn.sendto(self.pickle_message(uselist_message))
            break
                
    def receive_message(self, recvd_message):
        reconstructed_message = pickle.loads(recvd_message)
        return reconstructed_message
	    
    def pickle_message(self, message):
        pickled_message = pickle.dumps(message)
        return pickled_message
        
    def construct_message(self, message_type, message, target):
        seq_str = '{:0>3}'.format(1)
        id_str = '{:0>10}'.format(0)
        target_str = '{:0>10}'.format(target)
        new_message = Message(seq_str, message_type, id_str, target_str, 
                              message)
        return new_message
        