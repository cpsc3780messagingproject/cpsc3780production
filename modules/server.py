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
        self.uniqueclients = set()
        self.peers = set()
        self.messages = {}
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))

    def activate():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.listen(1)
            conn, addr = s.accept()
            # This could be understood as the 'main' function of the server.
            # Routing logic, listening, etc. will all be done when 
            # server.activate() is called. Note that the server constructs
            # its socket upon __init__ currently; I'm not sure if this is
            # actually an intelligent way to construct the class - we may
            # want to move s.bind() to server.activate().