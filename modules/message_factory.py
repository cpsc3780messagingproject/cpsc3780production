from modules.message import Message

def construct_message(message_type, sequence, senderid, targetid, message):
        MESSAGE_TYPES = { 
        0:      'SRV', #used for client-to-server communication
        1:      'SND', #used to send a message to server
        2:      'GET', #used to receive all messages from server
        3:      'ACK', #used to acknowledge receipt of messages
        4:      'USR', #indicates a server is sending a client a userlist
        5:      'ASN', #server is assigning a value to a client
        6:      'IDR', #client is first connecting; requesting id
        10:     'OFF'  #client is signing off
        }
        seq_str = '{:0>3}'.format(sequence)
        id_str = '{:0>10}'.format(senderid)
        target_str = '{:0>10}'.format(targetid)
        
        new_message = Message(seq_str, MESSAGE_TYPES[message_type], id_str, target_str, 
                              message)
        return new_message