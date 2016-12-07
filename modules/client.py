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

import thread
import time
import socket
import pickle
from modules.message import Message
from modules.message_factory import construct_message

"""class sendThread (threading.thread):
    def __init__(self, clientsocket, server, sequence, id):
        self.clientsocket = clientsocket
        self.server = server
        self.sequence = sequence
        self.id = id
        
    def run(self):
            while True:
                targ_id = raw_input("Please input the user to send to: ")
                raw_msg = raw_input("Please input a message to transmit: ")
                wrapped_msg = construct_message(1, self.sequence, self.id, 0, raw_msg) 
                while True:
                    s.sendto(pickle.dumps(wrapped_msg), (self.server, 5000))
                    data, garbagecatch = s.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    if (unpickled_data.type == 'ACK'):
                        break
                    else:
                        time.sleep(1)
                
                self.sequence = self.sequence + 1
                continue_flag = raw_input("Send another message? (y/n)")
                if (continue_flag == 'n'):
                    break
    
class getThread (threading.thread):
    def __init__(self, clientsocket, server, id):
        self.clientsocket = clientsocket
        self.server = server
        self.id = id
        
    def run(self):
        pass
        
"""
class MessageClient():
    def __init__(self, threadName, server):
        self.messages = []
        self.host = server
        self.mess_seq = 0
        self.id = 0
    
    def sendThread(self, threadName, flags):
        while True:
            targ_id = raw_input("Please input the user to send to: ")
            raw_msg = raw_input("Please input a message to transmit: ")
            wrapped_msg = construct_message(1, self.mess_seq, self.id, 0, raw_msg) 
            while True:
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                data, garbagecatch = s.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                if (unpickled_data.type == 'ACK'):
                    break
                else:
                    time.sleep(1)
            
            self.sequence = self.sequence + 1
            continue_flag = raw_input("Send another message? (y/n)")
            if (continue_flag == 'n'):
                break
    
    def getThread(self, delay):
        pass
    
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
                unpickled_data = pickle.loads(data)
                wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                print("Userlist: ", unpickled_data.payload)
                
            thread.start_new_thread(sendThread, ("Thread1", "this is bullshit"))
            thread.start_new_thread(getThread, ("Thread2", 3))