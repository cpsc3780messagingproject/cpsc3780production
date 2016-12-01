##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   message.py:
#       Simple c-style structure implemented using python classes. All
#       messages sent using Seiren are passed as Message() objects.
##############################################################################

class Message:
    def __init__(self, sequence, type, source, destination, payload):
        self.seq = sequence
        self.type = type
        self.source = source
        self.destination = destination
        self.payload = payload