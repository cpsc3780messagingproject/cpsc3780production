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
        self.rank = '0'
                        
        self.upperpeer = ['0', ""]
        self.lowerpeer = ['0', ""]                                      
        self.client_list = {}
        self.messages = []


    def activate(self, peer):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))
        setup = True
        if (peer != '0' and setup == True):
            wrapped_msg = construct_message(0,0,0,0,"Requesting access;" + self.host)          
            s.sendto(pickle.dumps(wrapped_msg), (peer, self.port))
            data, addr = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            peerinfo = unpickled_data.payload.split(";")
            self.rank = peerinfo[0]
            self.lowerpeer = [peerinfo[1],peerinfo[2]]
            self.upperpeer = [peerinfo[3],peerinfo[4]]
            wrapped_msg = construct_message(0,0,0,0,"New peer;" + self.host + ";" + self.rank)
            s.sendto(pickle.dumps(wrapped_msg), (self.lowerpeer[1], self.port))
            setup = False
        while True:
            data, addr = s.recvfrom(65536)
            print ("Connected by ", addr)
            unpickled_data = pickle.loads(data)
            print ("Client sent ", unpickled_data.type, unpickled_data.payload)
            if (unpickled_data.type == 'SRV'):  
                servmessage = unpickled_data.payload.split(";")
                if (servmessage[0] == "Requesting access"):
                    if (int(self.upperpeer[0]) > 0):
                        s.sendto(pickle.dumps(unpickled_data), (self.upperpeer[1], self.port))

                    elif (int(self.upperpeer[0]) == 0):
                        
                        wrapped_msg = construct_message(0,0,0,0, str(int(self.rank)+1) + ";" + self.rank + ";" + self.host + ";" + self.upperpeer[0] + ";" + self.upperpeer[1])
                        s.sendto(pickle.dumps(wrapped_msg), (servmessage[1], self.port))
                        self.upperpeer = [str(int(self.rank)+1),servmessage[1]]

                elif (servmessage[0] == "New peer"):
                    self.lowerpeer[0] = [servmessage[1],servmessage[0]]  
                
                elif (servmessage[0] == "Routed message"):
                    iterations = 0
                    highest_hops = 0                    
                    while True:
                        try:
                            index_tester = servmessage[2+(iterations*3)]
                        except IndexError:
                            break
                        for key[x,y,z] in self.client_list:
                            if (key == servmessage[1+(iterations*3)]):
                                if ((int(servmessage[2+(iterations*3)]) + 1) < key[1]):
                                    y = int(servmessage[2+(iterations*3)]) + 1  
                                    z = servmessage[3+(iterations*3)]
                                if ((int(servmessage(2+iterations*3)) + 1) > highest_hops):
                                    highest_hops = (int(servmessage(2+iterations*3)) + 1)
                        iterations += 1
                    if (self.rank == "0" and highest_hops < (int(self.rank) + int(self.lowerpeer[0]))):                           
                        formatted_clientlist = "" 
                        for key[x,y,z] in self.client_list:
                            formatted_clientlist += x + ";" + str(y) + ";" + z + ";"
                        wrapped_msg = construct_message(0,0,0,0,formatted_clientlist)
                        s.sendto(pickle.dumps(wrapped_msg), (self.lowerpeer[1], self.port))
                        s.sendto(pickle.dumps(wrapped_msg), (self.upperpeer[1], self.port))
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
                for key, (valx, _, _) in self.client_list.iteritems():  
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
                    self.client_list[unpickled_data.source] = (addr[0], 0, self.host)
                    formatted_clientlist = "" 
                    for key, (x,y,z) in self.client_list.iteritems():
                        formatted_clientlist += x + ";" + str(y) + ";" + z + ";"
                    wrapped_msg = construct_message(0,0,0,0,formatted_clientlist)
                    s.sendto(pickle.dumps(wrapped_msg), (self.lowerpeer[1], self.port))
                    s.sendto(pickle.dumps(wrapped_msg), (self.upperpeer[1], self.port))
                    wrapped_msg = construct_message(3,0,0, unpickled_data.source, "Welcome, " + unpickled_data.source + "!")
                    s.sendto(pickle.dumps(wrapped_msg), (addr))

   
 
