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
import threading
        
class MessageClient():
    def __init__(self, server):
        self.host = server
        self.mess_seq = 0
        self.id = 0
        self.messages = ()
    
    def activate(self):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if (self.id == 0):
            """wrapped_msg = construct_message(6, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            data, catchgarbage = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            print (unpickled_data.payload, "/n")
            self.id = unpickled_data.destination
            print("Your assigned ID is: ", self.id)"""
            while True:
                while True:
                    self.id = raw_input("Please input a handle (max 10 characters): ")
                    if (len(self.id) > 10):
                        print ("Handle is too long. Please choose another handle.")
                    else:
                        break
                wrapped_msg = construct_message(6, 0, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                
                data, garbagecatch = s.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                if (unpickled_data.type == 'ACK'):
                    print (unpickled_data.payload)
                    break
                else:
                    print (unpickled_data.payload)
            
            
            
            wrapped_msg = construct_message(4, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            data, catchgarbage = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            print("Userlist: ", unpickled_data.payload)

            
        while True:
            action_flag = raw_input("Please choose an action [s to send, c to check messages, e to exit]: ")
            if (action_flag == 's'):
                targ_id = raw_input("Please input the user to send to: ")
                raw_msg = raw_input("Please input a message to transmit: ")
                wrapped_msg = construct_message(1, self.mess_seq, self.id, targ_id, raw_msg) 
                while True:
                    s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                    data, garbagecatch = s.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    if (unpickled_data.type == 'ACK'):
                        break
                    else:
                        time.sleep(1)
                        pass
                self.mess_seq = self.mess_seq + 1
            elif (action_flag == 'n'):
                print("Signing off. Have a nice day!")
                break
            elif (continue_flag == 'c'):
                print ("Receiving messages: ")
                wrapped_msg = construct_message(2, 0, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                while True:
                    data, garbagecatch = s.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
                    s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                    if (unpickled_data.type == "EOM"):
                        break
                    else:
                        print (unpickled_data.source, " has sent:", unpickled_data.payload)
                        
        return