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

"""class sendThread (threading.Thread):
    def __init__(self, clientsocket, server, sequence, id, lock):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.server = server
        self.sequence = sequence
        self.id = id
        self.lock = lock
        self.messages = {}
        
    def run(self):
            while True:
                self.lock.acquire()
                targ_id = raw_input("Please input the user to send to: ")
                raw_msg = raw_input("Please input a message to transmit: ")
                wrapped_msg = construct_message(1, self.sequence, self.id, 0, raw_msg) 
                while True:
                    self.clientsocket.sendto(pickle.dumps(wrapped_msg), (self.server, 5000))
                    data, garbagecatch = self.clientsocket.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    if (unpickled_data.type == 'ACK'):
                        break
                    else:
                        time.sleep(1)
                self.lock.release()
                self.sequence = self.sequence + 1
                
                self.lock.acquire()
                continue_flag = raw_input("Send another message? (y/n)")
                if (continue_flag == 'n'):
                    break

                self.lock.release()
    
class getThread (threading.Thread):
    def __init__(self, clientsocket, server, id, lock):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.server = server
        self.id = id
        self.lock = lock
        
    def run(self):
        while True:
            print ("check0")
            time.sleep(3)
            print ("check1")
            self.lock.acquire()
            print ("Receiving messages: \n")
            wrapped_msg = construct_message(2, 0, self.id, 0, "")
            self.clientsocket.sendto(pickle.dumps(wrapped_msg), (self.server, 5000))
            print ("check2")
            while True:
                data, garbagecatch = self.clientsocket.recvfrom(65536)
                unpickled_data = pickle.loads(data)
                if (unpickled_data.payload() == ""):
                    break #this will eventually be the server's way of signalling "end of messages" - probably won't be an empty payload tho
                else:
                    self.messages[unpickled.data.seq] = unpickled_data
            self.lock.release()"""
        
class MessageClient():
    def __init__(self, server):
        self.host = server
        self.mess_seq = 0
        self.id = 0
        self.messages = ()
    
    def activate(self):
        """class sendThread (threading.Thread):
            def __init__(self, clientsocket, server, sequence, id):
                threading.Thread.__init__(self)
                self.clientsocket = clientsocket
                self.server = server
                self.sequence = sequence
                self.id = id
                self.messages = {}
        
            def run(self):
                while True:
                    threadLock.acquire()
                    targ_id = raw_input("Please input the user to send to: ")
                    raw_msg = raw_input("Please input a message to transmit: ")
                    wrapped_msg = construct_message(1, self.sequence, self.id, 0, raw_msg) 
                    while True:
                        self.clientsocket.sendto(pickle.dumps(wrapped_msg), (self.server, 5000))
                        data, garbagecatch = self.clientsocket.recvfrom(65536)
                        unpickled_data = pickle.loads(data)
                        if (unpickled_data.type == 'ACK'):
                            break
                        else:
                            time.sleep(1)
                    threadLock.release()
                    time.sleep(1)
                    self.sequence = self.sequence + 1
                    threadLock.acquire()
                    continue_flag = raw_input("Continue sending messages? (y/n)")
                    if (continue_flag == 'n'):
                        exit_flag = True
                        threadLock.release()
                        break
                    threadLock.release()
    
        class getThread (threading.Thread):
            def __init__(self, clientsocket, server, id):
                threading.Thread.__init__(self)
                self.clientsocket = clientsocket
                self.server = server
                self.id = id
                self.messages = []
        
            def run(self):
                while True:
                    if (exit_flag == True):
                        break
                    if (get_blocker == True):
                        pass
                    else:
                        print ("Receiving messages: \n")
                        wrapped_msg = construct_message(2, 0, self.id, 0, "")
                        self.clientsocket.sendto(pickle.dumps(wrapped_msg), (self.server, 5000))
                        while True:
                            data, garbagecatch = self.clientsocket.recvfrom(65536)
                            unpickled_data = pickle.loads(data)
                            if (unpickled_data.payload() == ""):
                                break #this will eventually be the server's way of signalling "end of messages" - probably won't be an empty payload tho
                            else:
                                self.messages[unpickled.data.seq] = unpickled_data"""
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if (self.id == 0):
            wrapped_msg = construct_message(6, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            data, catchgarbage = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            print (unpickled_data.payload, "/n")
            self.id = unpickled_data.destination
            print("Your assigned ID is: ", self.id)
            wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            data, catchgarbage = s.recvfrom(65536)
            unpickled_data = pickle.loads(data)
            wrapped_msg = construct_message(3, self.mess_seq, self.id, 0, "")
            s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
            print("Userlist: ", unpickled_data.payload)

            
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
                    pass
            self.mess_seq = self.mess_seq + 1
            continue_flag = raw_input("Continue sending messages? (y/n/c to check messages)")
            if (continue_flag == 'n'):
                break
            elif (continue_flag == 'c'):
                print ("Receiving messages: ")
                wrapped_msg = construct_message(2, 0, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                while True:
                    data, garbagecatch = s.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    if (unpickled_data.payload() == ""):
                        break #this will eventually be the server's way of signalling "end of messages" - probably won't be an empty payload tho
                    else:
                        self.messages[unpickled.data.seq] = unpickled_data
                for key in self.messages:
                    print (self.messages[key].payload, "\n")
            else:
                print ("Receiving messages: ")
                wrapped_msg = construct_message(2, 0, self.id, 0, "")
                s.sendto(pickle.dumps(wrapped_msg), (self.host, 5000))
                while True:
                    data, garbagecatch = s.recvfrom(65536)
                    unpickled_data = pickle.loads(data)
                    if (unpickled_data.payload() == "End of messages."):
                        break
                    else:
                        self.messages[unpickled.data.seq] = unpickled_data
                for key in self.messages:
                    print (self.messages[key].payload, "\n")
            

        return