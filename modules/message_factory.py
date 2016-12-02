from modules.message import Message

def construct_message(message_type, sequence, senderid, targetid, message):
        seq_str = '{:0>3}'.format(sequence)
        id_str = '{:0>10}'.format(senderid)
        target_str = '{:0>10}'.format(targetid)
        new_message = Message(seq_str, message_type, id_str, target_str, 
                              message)
        return new_message