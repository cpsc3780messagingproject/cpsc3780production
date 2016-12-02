##############################################################################
# Seiren : Simple Python Messaging Network
# CPSC 3780 Project
# Authors: Tyler Bertram, Jarvis Zazalack
#   A simple, object-oriented and dynamically-constructed messaging network
#   using UDP to pass message strings while handling small-scale routing
#   between multiple networks.
#
#   main.py:
#       Main program sequence, handles the actual running of the network
#       using the client, server and message objects.
#
#   Third-party resources used:
#       x
#       y
#       z
##############################################################################

from modules import message
from modules import server
from modules import client

while True:
    mode = raw_input("Run in server mode? [y/n]")
    if mode is "y":
        print("Running in server mode.")
        #net_serv = input("Please enter the IP address of at least one other 
        #                  server on desired network (0 to run as a sole 
        #                  server)."
        seiren_server = MessageServer(30019)
        seiren_server.activate()
        
        # Run in server mode. Probably fairly lightweight code.

        # Construct new MessageServer() object.
        
        break

    if mode is "n":
        print("Running in client mode.")
        hostname = raw_input("Input the IP address of the desired server: ")
        # Run in client mode. Takes inputs, sends messages. More complicated.

        # Construct new MessageClient() object.
        seiren_client = MessageClient(hostname)
        
        #Receive userlist from server upon connecting.
        #Get input from user, conver to message.
        #Send message. Wait for response x time - if no ACK, resend message.\
        #Block until ACK received.
        #Every x seconds, send GET to receive all messages.
        #This SHOULD be basically all the client needs to do.
        
        break

exit()