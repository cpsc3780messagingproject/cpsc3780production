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
import random
from modules.message import Message
from modules.message_factory import construct_message

class MessageServer():
    def __init__(self, port):
        self.host = '142.66.140.69'
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
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))


        while True:
            data, addr = s.recvfrom(65536)
            print ("Connected by ", addr)
            unpickled_data = pickle.loads(data)
            print ("Client sent ", unpickled_data.type, unpickled_data.payload)
#            if (unpickled_data.type == 'SRV'):       
            if (unpickled_data.type == 'SND'):
                self.messages.append(unpickled_data)
                wrapped_msg = construct_message(3,0,0,unpickled_data.source, "Message received!")
                s.sendto(pickle.dumps(wrapped_msg), (addr))

            elif (unpickled_data.type == 'GET'):
                while True:
                    if (self.messages.index(unpickled_data.source) == True):
                        message = self.messages.pop([self.messages.index(unpickled_data.source)])
                        data, addr = s.recvfrom(65536)
                    else:
                        break
                
#            elif (unpickled_data.type == 'ACK'):
            #forward message from client A to client B
                
            elif (unpickled_data.type == 'IDR'):               
                if (addr in self.client_list):
                    print("Welcome back, user!")
                else:
                    new_id = random.randint(1, 100000000)  
                    while True:
                        if (new_id in self.client_list):
                            new_id = randint(1, 1000000000)
                        else:
                            break
                    print("Sending new ID to user...")
                    self.client_list[new_id] = (addr[0],self.host)
                    wrapped_msg = construct_message(5, 0, 0, new_id, "")
                    s.sendto(pickle.dumps(wrapped_msg), (addr))
                    data, addr = s.recvfrom(65536)
                    clientstring = ""
                    for key in self.client_list:
                        clientstring += ('{:0>10}'.format(key)+ " ")
                    print("Sending client list to user...")
                    wrapped_msg = construct_message(4, 0, 0, new_id, clientstring) 
                    s.sendto(pickle.dumps(wrapped_msg), (addr))    
