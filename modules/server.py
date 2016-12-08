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
    def __init__(self, port, ip):
        self.host = ip
        self.port = port
        self.rank = 0                       # Rank is used to determine which
        self.peerlist = []                  # other server the server should
                                            # talk to when updating client
                                            # lists. While it always starts at
                                            # 0, upon hooking a server into a
                                            # network, it will slot itself
                                            # into the highest open rank. 
        self.client_list = {}
        self.messages = []


    def activate(self, peer):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))
        if (peer != 0):
            wrapped_msg = construct_message(0,0,0,0,"Requesting access;")          
            s.sendto(pickle.dumps(wrapped_msg), (peer, port))
            data, addr = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            peerinfo = unpickled_data.payload.split(";")
            self.rank = peerinfo[0]
            self.peerlist.append(peerinfo[1],peerinfo[2])
            self.peerlist.append(peerinfo[3],peerinfo[4])
            wrapped_msg = construct_message(0,0,0,0,"New peer;" + self.host + ";" + self.rank)
        while True:
            data, addr = s.recvfrom(65536)
            print ("Connected by ", addr)
            unpickled_data = pickle.loads(data)
            print ("Client sent ", unpickled_data.type, unpickled_data.payload)
            if (unpickled_data.type == 'SRV'):  
                servmessage = unpickled_data.payload.split(";")
                   
                if (servmessage[0] == "Requesting access")
                    wrapped_message = construct_message(0,0,0,0, (self.rank+1) + ";" + 
                elif (servmessage[0] == "New peer")
                    
            elif (unpickled_data.type == 'SND'):
                self.messages.append(unpickled_data)
                wrapped_msg = construct_message(3,0,0,unpickled_data.source, "Message received!")
                s.sendto(pickle.dumps(wrapped_msg), (addr))

            elif (unpickled_data.type == 'GET'):
                for x in self.messages:
                    print (x.destination)
                    if (x.destination == unpickled_data.source):
                        message = self.messages.pop(self.messages.index(x))
                        messagedest = self.client_list[message.destination]
                        s.sendto(pickle.dumps(message), (addr))
                        data, addr = s.recvfrom(65536)
                wrapped_msg = construct_message(9,0,0, unpickled_data.source, "")
                s.sendto(pickle.dumps(wrapped_msg), (addr))
                
            elif (unpickled_data.type == 'USR'):
                clientstring = ""
                for key in self.client_list:
                    clientstring += key + ", "
                print("Sending client list to user...")
                wrapped_msg = construct_message(4, 0, 0, unpickled_data.source, clientstring) 
                s.sendto(pickle.dumps(wrapped_msg), (addr))

#            elif (unpickled_data.type == 'ACK'):
            #forward ack from client A to client B
                
            elif (unpickled_data.type == 'IDS'): 
                exists = False
                taken = False       
                for key, (valx, _) in self.client_list.iteritems():  
                    if (key == unpickled_data.source):
                        if (valx == addr[0]):
                            exists = True
                            break
                        else:
                            taken = True
                            break
                if (exists == True):   
                    wrapped_msg = construct_message(3,0,0, unpickled_data.source, "Welcome back, " + unpickled_data.source + "!")
                    s.sendto(pickle.dumps(wrapped_msg), (addr))
                elif(taken == True):
                    wrapped_msg = construct_message(6,0,0, unpickled_data.source, "Handle taken! Try again.")
                    s.sendto(pickle.dumps(wrapped_msg), (addr))  
                else:
                    self.client_list[unpickled_data.source] = (addr[0], self.host)
                    wrapped_msg = construct_message(3,0,0, unpickled_data.source, "Welcome, " + unpickled_data.source + "!")
                    s.sendto(pickle.dumps(wrapped_msg), (addr))

   
 
