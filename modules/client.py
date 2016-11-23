import socket
import pickle
from message import Message

class MessageClient():
    def __init__(self, port):
        self.host = ''
        self.port = port
        self.mess_seq = 0
        
        random.seed(None)
        self.id = randint(1, 1000000000)
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))

    def send(self, message, target):

        return null # to get annoying red lines out of the way rn

    def construct_message(self, message_type, message, target):
        seq_str = '{:0>3}'.format(self.mess_seq)
        id_str = '{:0>10}'.format(self.id)
        target_str = '{:0>10}'.format(target)
        new_message = Message(seq_str, message_type, id_str, target_str, 
                              message)
        return new_message
        