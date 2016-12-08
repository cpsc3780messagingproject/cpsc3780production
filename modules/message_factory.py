##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   message_factory.py:
#       Function for creating message objects, used in multiple places.
##############################################################################

from modules.message import Message

def construct_message(message_type, sequence, senderid, targetid, message):
        MESSAGE_TYPES = { 
        0:      'SRV', #used for client-to-server communication
        1:      'SND', #used to send a message to server
        2:      'GET', #used to receive all messages from server
        3:      'ACK', #used to acknowledge receipt of messages
        4:      'USR', #used for userlist transactions
        5:      'ASN', #server is assigning a value to a client - deprecated
        6:      'IDS', #client is first connecting; submitting id
        9:      'EOM'  #server is sending end of messages flag
        }
        seq_str = '{:0>3}'.format(sequence)
        #id_str = '{:0>10}'.format(senderid)
        #target_str = '{:0>10}'.format(targetid)
        
        new_message = Message(seq_str, MESSAGE_TYPES[message_type], senderid, targetid, 
                              message)
        return new_message
